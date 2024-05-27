import os
import xmltodict

def load_xml(file_path):
    """Load data from an XML file."""
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None

    try:
        with open(file_path, 'r') as file:
            xml_string = file.read()
            data = xmltodict.parse(xml_string)
        print("XML data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error with loading XML: {e}")
        return None