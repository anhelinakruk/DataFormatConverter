import argparse
from json_operations import load_json, save_json
from yml_operations import load_yaml, save_yaml

def parse_arguments():
    parser = argparse.ArgumentParser(description="Program for data conversion supporting .xml, .json, and .yml (.yaml) formats")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the output file")
    return parser.parse_args()

def main():
    args = parse_arguments()
    input_file = args.input_file
    output_file = args.output_file

    if input_file.lower().endswith('.json'):
        load_function = load_json
    elif input_file.lower().endswith('.yaml') or input_file.lower().endswith('.yml'):
        load_function = load_yaml
    else:
        print("Unsupported file format. Currently, only .json, .yaml/.yml formats.")
        return
   
    data = load_function(input_file)
    if data is None:
        print("Failed to load data.")
        return
    
    if output_file.lower().endswith('.json'):
        save_json(data, output_file)
    elif output_file.lower().endswith('.yaml') or output_file.lower().endswith('.yml'):
        save_yaml(data, output_file)
    else:
        print("Unsupported file format. Currently, only .json, .yaml/.yml formats.")
        return
    print(f"Data successfully saved to {output_file}")
    
if __name__ == "__main__":
    main()
    
