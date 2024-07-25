import json

def calculate_velocity(distance: float, time: float) -> float:
    """Calculate velocity given distance and time."""
    if time == 0:
        raise ValueError("Time cannot be zero.")
    return distance / time

calculate_velocity.schema = json.dumps({
    "name": "calculate_velocity",
    "description": "Calculate velocity given distance and time",
    "category": "physics",
    "parameters": {
        "type": "object",
        "properties": {
            "distance": {"type": "number", "description": "Distance traveled in meters"},
            "time": {"type": "number", "description": "Time taken in seconds"}
        },
        "required": ["distance", "time"]
    }
})

def convert_temperature(temperature: float, from_scale: str, to_scale: str) -> float:
    """Convert temperature between Celsius, Fahrenheit, and Kelvin."""
    scales = ['celsius', 'fahrenheit', 'kelvin']
    if from_scale.lower() not in scales or to_scale.lower() not in scales:
        raise ValueError("Invalid temperature scale. Use 'celsius', 'fahrenheit', or 'kelvin'.")
    
    # Convert to Celsius first
    if from_scale.lower() == 'fahrenheit':
        celsius = (temperature - 32) * 5/9
    elif from_scale.lower() == 'kelvin':
        celsius = temperature - 273.15
    else:
        celsius = temperature
    
    # Convert from Celsius to desired scale
    if to_scale.lower() == 'fahrenheit':
        return celsius * 9/5 + 32
    elif to_scale.lower() == 'kelvin':
        return celsius + 273.15
    else:
        return celsius

convert_temperature.schema = json.dumps({
    "name": "convert_temperature",
    "description": "Convert temperature between Celsius, Fahrenheit, and Kelvin",
    "category": "physics",
    "parameters": {
        "type": "object",
        "properties": {
            "temperature": {"type": "number", "description": "Temperature value to convert"},
            "from_scale": {"type": "string", "description": "Original temperature scale ('celsius', 'fahrenheit', or 'kelvin')"},
            "to_scale": {"type": "string", "description": "Desired temperature scale ('celsius', 'fahrenheit', or 'kelvin')"}
        },
        "required": ["temperature", "from_scale", "to_scale"]
    }
})

def calculate_force(mass: float, acceleration: float) -> float:
    """Calculate force using Newton's Second Law: F = ma."""
    return mass * acceleration

calculate_force.schema = json.dumps({
    "name": "calculate_force",
    "description": "Calculate force using Newton's Second Law: F = ma",
    "category": "physics",
    "parameters": {
        "type": "object",
        "properties": {
            "mass": {"type": "number", "description": "Mass of the object in kilograms"},
            "acceleration": {"type": "number", "description": "Acceleration of the object in meters per second squared"}
        },
        "required": ["mass", "acceleration"]
    }
})