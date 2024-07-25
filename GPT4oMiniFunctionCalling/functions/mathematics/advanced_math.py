import json

def calculate_factorial(n: int) -> int:
    """Calculate the factorial of a number"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n-1)

calculate_factorial.schema = json.dumps({
    "name": "calculate_factorial",
    "description": "Calculate the factorial of a number",
    "category": "mathematics",  # Added category
    "parameters": {
        "type": "object",
        "properties": {
            "n": {"type": "integer", "description": "The number to calculate factorial for"}
        },
        "required": ["n"]
    }
})

def fibonacci_sequence(n: int) -> list:
    """Generate Fibonacci sequence up to n terms"""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

fibonacci_sequence.schema = json.dumps({
    "name": "fibonacci_sequence",
    "description": "Generate Fibonacci sequence up to n terms",
    "category": "mathematics",  # Added category
    "parameters": {
        "type": "object",
        "properties": {
            "n": {"type": "integer", "description": "Number of terms in the sequence"}
        },
        "required": ["n"]
    }
})