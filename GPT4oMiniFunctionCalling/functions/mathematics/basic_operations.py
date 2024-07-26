# import json
# import math

# def add(a: float, b: float) -> float:
#     """Add two numbers"""
#     print(f"Add function called with a: {a}, b: {b}")
#     result = a + b
#     print(f"Add function result: {result}")
#     return result

# add.schema = json.dumps({
#     "name": "add",
#     "description": "Add two numbers",
#     "category": "mathematics",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "a": {"type": "number", "description": "First number to add"},
#             "b": {"type": "number", "description": "Second number to add"}
#         },
#         "required": ["a", "b"]
#     }
# })

# def subtract(a: float, b: float) -> float:
#     """Subtract two numbers"""
#     print(f"Subtract function called with a: {a}, b: {b}")
#     result = a - b
#     print(f"Subtract function result: {result}")
#     return result

# subtract.schema = json.dumps({
#     "name": "subtract",
#     "description": "Subtract two numbers",
#     "category": "mathematics",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "a": {"type": "number", "description": "Number to subtract from"},
#             "b": {"type": "number", "description": "Number to subtract"}
#         },
#         "required": ["a", "b"]
#     }
# })

# def multiply(a: float, b: float) -> float:
#     """Multiply two numbers"""
#     print(f"Multiply function called with a: {a}, b: {b}")
#     result = a * b
#     print(f"Multiply function result: {result}")
#     return result

# multiply.schema = json.dumps({
#     "name": "multiply",
#     "description": "Multiply two numbers",
#     "category": "mathematics",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "a": {"type": "number", "description": "First number to multiply"},
#             "b": {"type": "number", "description": "Second number to multiply"}
#         },
#         "required": ["a", "b"]
#     }
# })

# def divide(a: float, b: float) -> float:
#     """Divide two numbers"""
#     print(f"Divide function called with a: {a}, b: {b}")
#     if b == 0:
#         raise ValueError("Cannot divide by zero")
#     result = a / b
#     print(f"Divide function result: {result}")
#     return result

# divide.schema = json.dumps({
#     "name": "divide",
#     "description": "Divide two numbers",
#     "category": "mathematics",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "a": {"type": "number", "description": "Number to be divided (numerator)"},
#             "b": {"type": "number", "description": "Number to divide by (denominator)"}
#         },
#         "required": ["a", "b"]
#     }
# })

# def square_root(a: float) -> float:
#     """Calculate the square root of a number"""
#     print(f"Square root function called with a: {a}")
#     if a < 0:
#         raise ValueError("Cannot calculate square root of a negative number")
#     result = math.sqrt(a)
#     print(f"Square root function result: {result}")
#     return result

# square_root.schema = json.dumps({
#     "name": "square_root",
#     "description": "Calculate the square root of a number",
#     "category": "mathematics",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "a": {"type": "number", "description": "Number to calculate the square root of"}
#         },
#         "required": ["a"]
#     }
# })

# def power(base: float, exponent: float) -> float:
#     """Calculate the power of a number"""
#     print(f"Power function called with base: {base}, exponent: {exponent}")
#     result = math.pow(base, exponent)
#     print(f"Power function result: {result}")
#     return result

# power.schema = json.dumps({
#     "name": "power",
#     "description": "Calculate the power of a number",
#     "category": "mathematics",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "base": {"type": "number", "description": "The base number"},
#             "exponent": {"type": "number", "description": "The exponent"}
#         },
#         "required": ["base", "exponent"]
#     }
# })

# def greater_than(a: float, b: float) -> bool:
#     """Check if the first number is greater than the second number"""
#     print(f"Greater than function called with a: {a}, b: {b}")
#     result = a > b
#     print(f"Greater than function result: {result}")
#     return result

# greater_than.schema = json.dumps({
#     "name": "greater_than",
#     "description": "Check if the first number is greater than the second number",
#     "category": "mathematics",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "a": {"type": "number", "description": "First number to compare"},
#             "b": {"type": "number", "description": "Second number to compare"}
#         },
#         "required": ["a", "b"]
#     }
# })

# def less_than(a: float, b: float) -> bool:
#     """Check if the first number is less than the second number"""
#     print(f"Less than function called with a: {a}, b: {b}")
#     result = a < b
#     print(f"Less than function result: {result}")
#     return result

# less_than.schema = json.dumps({
#     "name": "less_than",
#     "description": "Check if the first number is less than the second number",
#     "category": "mathematics",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "a": {"type": "number", "description": "First number to compare"},
#             "b": {"type": "number", "description": "Second number to compare"}
#         },
#         "required": ["a", "b"]
#     }
# })


import json
import math

def add(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b

add.schema = json.dumps({
    "name": "add",
    "description": "Add two numbers",
    "category": "mathematics",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "number", "description": "First number to add"},
            "b": {"type": "number", "description": "Second number to add"}
        },
        "required": ["a", "b"]
    }
})

def subtract(a: float, b: float) -> float:
    """Subtract two numbers"""
    return a - b

subtract.schema = json.dumps({
    "name": "subtract",
    "description": "Subtract two numbers",
    "category": "mathematics",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "number", "description": "Number to subtract from"},
            "b": {"type": "number", "description": "Number to subtract"}
        },
        "required": ["a", "b"]
    }
})

def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b

multiply.schema = json.dumps({
    "name": "multiply",
    "description": "Multiply two numbers",
    "category": "mathematics",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "number", "description": "First number to multiply"},
            "b": {"type": "number", "description": "Second number to multiply"}
        },
        "required": ["a", "b"]
    }
})

def divide(a: float, b: float) -> float:
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

divide.schema = json.dumps({
    "name": "divide",
    "description": "Divide two numbers",
    "category": "mathematics",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "number", "description": "Number to be divided (numerator)"},
            "b": {"type": "number", "description": "Number to divide by (denominator)"}
        },
        "required": ["a", "b"]
    }
})

def square_root(a: float) -> float:
    """Calculate the square root of a number"""
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(a)

square_root.schema = json.dumps({
    "name": "square_root",
    "description": "Calculate the square root of a number",
    "category": "mathematics",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "number", "description": "Number to calculate the square root of"}
        },
        "required": ["a"]
    }
})

def power(base: float, exponent: float) -> float:
    """Calculate the power of a number"""
    print(f"Power function called with base: {base}, exponent: {exponent}")
    result = math.pow(base, exponent)
    print(f"Power function result: {result}")
    return result

power.schema = json.dumps({
    "name": "power",
    "description": "Calculate the power of a number",
    "category": "mathematics",
    "parameters": {
        "type": "object",
        "properties": {
            "base": {"type": "number", "description": "The base number"},
            "exponent": {"type": "number", "description": "The exponent"}
        },
        "required": ["base", "exponent"]
    }
})

def greater_than(a: float, b: float) -> bool:
    """Check if the first number is greater than the second number"""
    return a > b

greater_than.schema = json.dumps({
    "name": "greater_than",
    "description": "Check if the first number is greater than the second number",
    "category": "mathematics",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "number", "description": "First number to compare"},
            "b": {"type": "number", "description": "Second number to compare"}
        },
        "required": ["a", "b"]
    }
})

def less_than(a: float, b: float) -> bool:
    """Check if the first number is less than the second number"""
    return a < b

less_than.schema = json.dumps({
    "name": "less_than",
    "description": "Check if the first number is less than the second number",
    "category": "mathematics",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "number", "description": "First number to compare"},
            "b": {"type": "number", "description": "Second number to compare"}
        },
        "required": ["a", "b"]
    }
})
