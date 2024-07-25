import importlib
import os
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

class FunctionManager:
    def __init__(self):
        self.functions = {}
        self.function_keywords = {}
        self.load_functions()
        self.functions['find_relevant_functions'] = self.find_relevant_functions_wrapper

    def load_functions(self):
        functions_dir = 'functions'
        for root, dirs, files in os.walk(functions_dir):
            for file in files:
                if file.endswith('.py') and file != '__init__.py':
                    module_path = os.path.join(root, file).replace('/', '.').replace('\\', '.')[:-3]
                    module = importlib.import_module(module_path)
                    for attr_name in dir(module):
                        attr = getattr(module, attr_name)
                        if callable(attr) and hasattr(attr, 'schema'):
                            self.functions[attr_name] = attr
        self.update_function_keywords()

    def generate_keywords(self, func_name, func_description):
        tokens = word_tokenize(func_name + " " + func_description)
        stop_words = set(stopwords.words('english'))
        keywords = [word.lower() for word in tokens if word.isalnum() and word.lower() not in stop_words]
        return list(set(keywords))  # Remove duplicates

    def update_function_keywords(self):
        self.function_keywords = {}
        for func_name, func in self.functions.items():
            schema = json.loads(func.schema)
            category = schema.get('category', 'general')
            description = schema.get('description', '')
            keywords = self.generate_keywords(func_name, description)
            
            if category not in self.function_keywords:
                self.function_keywords[category] = {}
            self.function_keywords[category][func_name] = keywords

    def get_all_function_schemas(self):
        schemas = []
        for func_name, func in self.functions.items():
            if hasattr(func, 'schema'):
                schema = json.loads(func.schema)
                if 'name' not in schema:
                    schema['name'] = func_name
                schemas.append({
                    "name": schema['name'],
                    "description": schema.get('description', f"Function {func_name}"),
                    "parameters": schema.get('parameters', {
                        "type": "object",
                        "properties": {},
                        "required": []
                    })
                })
            else:
                schemas.append({
                    "name": func_name,
                    "description": f"Function {func_name}",
                    "parameters": {
                        "type": "object",
                        "properties": {},
                        "required": []
                    }
                })
        return schemas

    def call_function(self, function_name, args):
        if function_name in self.functions:
            return self.functions[function_name](**args)
        else:
            raise ValueError(f"Function {function_name} not found")

    def find_relevant_functions(self, query: str) -> list:
        """Find relevant functions based on the query"""
        query_words = set(self.generate_keywords(query, ""))
        relevant_functions = []

        for category, functions in self.function_keywords.items():
            for func_name, keywords in functions.items():
                if query_words.intersection(keywords):
                    relevant_functions.append({"name": func_name, "category": category})

        return relevant_functions

    def get_function_details(self, func_list: list) -> str:
        """Get a formatted string of function details"""
        if not func_list:
            return "No specific functions found. You may need to rephrase your query."

        details = "Relevant functions:\n"
        for func in func_list:
            schema = json.loads(self.functions[func['name']].schema)
            details += f"- {func['name']} (Category: {func['category']})\n"
            details += f"  Description: {schema.get('description', 'No description available')}\n"
        return details

    def find_relevant_functions_wrapper(self, query: str) -> str:
        """Wrapper function to find relevant functions and return their details"""
        relevant_funcs = self.find_relevant_functions(query)
        details = self.get_function_details(relevant_funcs)
        return details if details else "No relevant functions found."

# Define the schema for the find_relevant_functions_wrapper
find_relevant_functions_schema = json.dumps({
    "name": "find_relevant_functions",
    "description": "Find relevant functions based on the user's query",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "The user's input query"
            }
        },
        "required": ["query"]
    }
})

# Attach the schema to the wrapper function
FunctionManager.find_relevant_functions_wrapper.schema = find_relevant_functions_schema