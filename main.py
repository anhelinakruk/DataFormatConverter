import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Program for data conversion supporting .xml, .json, and .yml (.yaml) formats")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the output file")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    print(f"Input file: {args.input_file}")
    print(f"Output file: {args.output_file}")