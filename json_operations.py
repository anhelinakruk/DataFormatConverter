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
    
def save_json(data, file_path):
    """Save data to a JSON file"""
    try:
        if not os.path.exists(file_path):
            directory = os.path.dirname(file_path)
            if directory:
                os.makedirs(directory, exist_ok=True)
            else:
                file_path = os.path.join(os.getcwd(), file_path)
                directory = os.path.dirname(file_path)
                os.makedirs(directory, exist_ok=True)
            with open(file_path, 'w') as file:
                file.write('{}\n')
            print(f"Created new JSON file: {file_path}")

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print("Data saved to JSON file successfully.")
    except Exception as e:
        print(f"Error with saving data to JSON file: {e}")
