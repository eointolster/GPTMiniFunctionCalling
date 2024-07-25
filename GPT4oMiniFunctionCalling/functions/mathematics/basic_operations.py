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
    return math.pow(base, exponent)

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