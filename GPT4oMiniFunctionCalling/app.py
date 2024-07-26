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
                model="gpt-4-0613",  # or "gpt-4" if you have access
                messages=messages,
                functions=function_manager.get_all_function_schemas(),
                function_call="auto",
            )
            
            response_message = response.choices[0].message

            # Check if there's a function call
            if response_message.function_call:
                function_name = response_message.function_call.name
                function_args = json.loads(response_message.function_call.arguments)
                print(f"Calling function: {function_name} with args: {function_args}")
                function_response = function_manager.call_function(function_name, function_args)
                print(f"Function response: {function_response}")
                
                # Convert the function response to a string
                if isinstance(function_response, bool):
                    function_response = str(function_response)
                elif not isinstance(function_response, str):
                    function_response = json.dumps(function_response)
                
                # Add the function call and result to the conversation
                messages.append({
                    "role": "function",
                    "name": function_name,
                    "content": function_response,
                })
                
                # Get AI's interpretation of the function result
                continue
            
            # If there's content in the response, add it to the conversation
            if response_message.content:
                messages.append({"role": "assistant", "content": response_message.content})
                return response_message.content

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
