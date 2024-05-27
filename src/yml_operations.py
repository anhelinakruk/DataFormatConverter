import yaml
import os 

def load_yaml(file_path):
    """Load data from a YAML file and verify its syntax."""
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None

    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except yaml.YAMLError as e:
        print(f"Error with decoding YAML: {e}")
        return None
    except Exception as e:
        print(f"Error with loading YAML: {e}")
        return None
    
def save_yaml(data, file_path):
    """Save data to a YAML file"""
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
                file.write('')
            print(f"Created new YAML file: {file_path}")

        with open(file_path, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
        print("Data saved to YAML file successfully.")
    except Exception as e:
        print(f"Error with saving data to YAML file: {e}")