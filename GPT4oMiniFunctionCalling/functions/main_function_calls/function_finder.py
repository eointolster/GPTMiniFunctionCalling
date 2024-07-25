import json
import re
from typing import List, Dict

# This dictionary maps keywords to function names and their categories
FUNCTION_KEYWORDS = {
    "mathematics": {
        "add": ["add", "sum", "plus", "addition", "combine"],
        "subtract": ["subtract", "minus", "difference", "take away"],
        "multiply": ["multiply", "times", "product"],
        "divide": ["divide", "division", "ratio"],
        "square_root": ["square root", "sqrt"],
        "power": ["power", "exponent", "raised to"],
        "calculate_factorial": ["factorial", "n!"],
        "fibonacci_sequence": ["fibonacci", "fib sequence"],
    },
    "science": {
        "calculate_velocity": ["velocity", "speed", "distance over time"],
        "convert_temperature": ["temperature", "celsius", "fahrenheit", "kelvin"],
        "calculate_force": ["force", "mass", "acceleration"],
    },
    # Add more categories and functions as needed
}

def find_relevant_functions(query: str) -> List[Dict[str, str]]:
    """
    Find relevant functions based on the query.
    
    Args:
    query (str): The user's input query.

    Returns:
    List[Dict[str, str]]: A list of dictionaries containing function names and their categories.
    """
    relevant_functions = []
    query_lower = query.lower()

    for category, functions in FUNCTION_KEYWORDS.items():
        for func_name, keywords in functions.items():
            if any(keyword in query_lower for keyword in keywords):
                relevant_functions.append({"name": func_name, "category": category})

    # If no specific functions are found, suggest the general math operations
    if not relevant_functions and any(word in query_lower for word in ["calculate", "compute", "math", "number"]):
        relevant_functions = [
            {"name": "add", "category": "mathematics"},
            {"name": "subtract", "category": "mathematics"},
            {"name": "multiply", "category": "mathematics"},
            {"name": "divide", "category": "mathematics"}
        ]

    return relevant_functions

def get_function_details(func_list: List[Dict[str, str]]) -> str:
    """
    Get a formatted string of function details.

    Args:
    func_list (List[Dict[str, str]]): List of dictionaries containing function names and categories.

    Returns:
    str: A formatted string describing the relevant functions.
    """
    if not func_list:
        return "No specific functions found. You may need to rephrase your query or use general math operations."

    details = "Relevant functions:\n"
    for func in func_list:
        details += f"- {func['name']} (Category: {func['category']})\n"
    return details

def find_relevant_functions_wrapper(query: str) -> str:
    """
    Wrapper function to find relevant functions and return their details.

    Args:
    query (str): The user's input query.

    Returns:
    str: A formatted string describing the relevant functions.
    """
    relevant_funcs = find_relevant_functions(query)
    return get_function_details(relevant_funcs)

# Define the schema for the OpenAI function calling API
find_relevant_functions_wrapper.schema = json.dumps({
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

