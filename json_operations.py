import os
import json

def load_json(file_path):
    """Load and parse data from a JSON file"""
    if not os.path.exists(file_path):
        print(f"File {file_path} not found")
        return None

    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Error with loading JSON: {e}")
        return None
    
