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
    max_function_calls = 10  # Set a maximum number of function calls
    function_call_count = 0

    while function_call_count < max_function_calls:
        print("Sending request to OpenAI")
        try:
            response = client.chat.completions.create(
                model="gpt-4-0613",
                messages=messages,
                functions=function_manager.get_all_function_schemas(),
                function_call="auto",
            )
            
            response_message = response.choices[0].message

            # Check if there's a function call
            if response_message.function_call:
                function_call_count += 1
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
                
                # Add a system message to encourage the AI to move to the next step
                messages.append({
                    "role": "system",
                    "content": "Please proceed to the next step in the calculation or provide the final result."
                })
                
                continue
            
            # If there's content in the response, add it to the conversation and return
            if response_message.content:
                messages.append({"role": "assistant", "content": response_message.content})
                return messages  # Return the entire conversation

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            error_message = f"I'm sorry, but an error occurred: {str(e)}"
            messages.append({"role": "assistant", "content": error_message})
            return messages  # Return the conversation with the error message

    # If we've reached the maximum number of function calls without a final response
    error_message = "I apologize, but I wasn't able to complete the calculation within the allowed number of steps. Please try rephrasing your request or breaking it down into smaller steps."
    messages.append({"role": "assistant", "content": error_message})
    return messages  # Return the conversation with the error message

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
            conversation = [
                {"role": "system", "content": "You are an AI assistant capable of performing mathematical operations. When given a sequence of operations, perform them step by step, using the result of each operation as input for the next. After each step, move on to the next operation until you reach the final result."},
                {"role": "user", "content": user_input}
            ]
        else:
            return jsonify({'error': 'Invalid request format'}), 400

        response = run_conversation(conversation)
        
        return jsonify({'conversation': response})
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500
    

if __name__ == '__main__':
    app.run(debug=True)
