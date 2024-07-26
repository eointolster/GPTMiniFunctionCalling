from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import json
from function_manager import FunctionManager, find_relevant_functions_schema
from function_manager import FunctionManager
import os
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

app = Flask(__name__)
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))  # Make sure to set this environment variable
function_manager = FunctionManager()

def run_conversation(conversation):
    print("Starting conversation")
    messages = conversation
    
    print("Setting up functions")

    while True:
        print("Sending request to OpenAI")
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # or "gpt-4" if you have access
                messages=messages,
                functions=function_manager.get_all_function_schemas(),
                function_call="auto",
            )
            
            response_message = response.choices[0].message

            # Check if there's content in the response
            if response_message.content:
                # Add the response to the conversation history
                messages.append({"role": "assistant", "content": response_message.content})

            # Check if there's a function call
            if response_message.function_call:
                function_name = response_message.function_call.name
                function_args = json.loads(response_message.function_call.arguments)
                function_response = function_manager.call_function(function_name, function_args)
                
                # Convert the function response to a string
                if isinstance(function_response, bool):
                    function_response = str(function_response)
                elif not isinstance(function_response, str):
                    function_response = json.dumps(function_response)
                
                messages.append(
                    {
                        "role": "function",
                        "name": function_name,
                        "content": function_response,
                    }
                )
                # Continue the conversation to get AI's response to the function output
                continue
            else:
                return response_message.content or "I'm sorry, I don't have a response for that."

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return f"I'm sorry, but an error occurred: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        if 'conversation' in request.json:
            conversation = request.json['conversation']
            if not conversation:
                return jsonify({'error': 'Conversation is empty'}), 400
            user_input = conversation[-1]['content']
        elif 'message' in request.json:
            user_input = request.json['message']
            conversation = [{"role": "user", "content": user_input}]
        else:
            return jsonify({'error': 'Invalid request format'}), 400

        response = run_conversation(conversation)
        
        if isinstance(response, str):
            conversation.append({"role": "assistant", "content": response})
        
        return jsonify({'conversation': conversation})
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500
if __name__ == '__main__':
    app.run(debug=True)
