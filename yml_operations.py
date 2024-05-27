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