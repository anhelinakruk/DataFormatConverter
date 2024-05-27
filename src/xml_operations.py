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
    
def save_xml(data, file_path):
    """Save data to an XML file."""
    try:
        root_key = next(iter(data))
        root_value = data[root_key]
        xml_data = {root_key: root_value}

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
            print(f"Created new XML file: {file_path}")


        xml_content = xmltodict.unparse(xml_data, pretty=True)
        with open(file_path, 'w') as file:
            file.write(xml_content)

        print(f"Data saved to XML file: {file_path}")

    except Exception as e:
        print(f"Error with saving XML: {e}")
