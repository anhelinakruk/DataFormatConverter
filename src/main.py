import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from json_operations import load_json, save_json
from yml_operations import load_yaml, save_yaml
from xml_operations import load_xml, save_xml

class DataConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Converter")

        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12), padding=10)
        self.style.configure('TLabel', font=('Helvetica', 12))

        self.mainframe = ttk.Frame(root, padding="10 10 10 10")
        self.mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        self.input_label = ttk.Label(self.mainframe, text="Input File (full route):")
        self.input_label.grid(column=1, row=1, sticky=tk.W)

        self.input_entry = ttk.Entry(self.mainframe, width=50)
        self.input_entry.grid(column=2, row=1, columnspan=2, sticky=(tk.W, tk.E))
        
        self.output_label = ttk.Label(self.mainframe, text="Output File:")
        self.output_label.grid(column=1, row=3, sticky=tk.W)
        
        self.output_entry = ttk.Entry(self.mainframe, width=50)
        self.output_entry.grid(column=2, row=3, sticky=(tk.W, tk.E))
        
        self.output_button = ttk.Button(self.mainframe, text="Browse", command=self.browse_output_file)
        self.output_button.grid(column=3, row=3, sticky=tk.W)

        self.convert_button = ttk.Button(self.mainframe, text="Convert", command=self.convert_data)
        self.convert_button.grid(column=2, row=4, sticky=tk.E)

        for child in self.mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        self.input_file = None

    def browse_output_file(self):
        try:
            output_file = filedialog.asksaveasfilename(filetypes=[
                ("All Files", "*.*"), 
                ("JSON Files", "*.json"), 
                ("YAML Files", "*.yaml;*.yml"), 
                ("XML Files", "*.xml")
            ])
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, output_file)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to select output file: {e}")

    def convert_data(self):
        input_file = self.input_entry.get()
        output_file = self.output_entry.get()

        if not input_file:
            messagebox.showerror("Error", "Please specify an input file.")
            return

        if not output_file:
            messagebox.showerror("Error", "Please specify an output file.")
            return

        try:
            if input_file.lower().endswith('.json'):
                load_function = load_json
            elif input_file.lower().endswith('.yaml') or input_file.lower().endswith('.yml'):
                load_function = load_yaml
            elif input_file.lower().endswith('.xml'):
                load_function = load_xml
            else:
                messagebox.showerror("Error", "Only .json, .yaml/.yml, and .xml formats are supported.")
                return

            data = load_function(input_file)
            if data is None:
                messagebox.showerror("Error", "Failed to load data.")
                return
            
            if output_file.lower().endswith('.json'):
                save_json(data, output_file)
            elif output_file.lower().endswith('.yaml') or output_file.lower().endswith('.yml'):
                save_yaml(data, output_file)
            elif output_file.lower().endswith('.xml'):
                adjusted_data = {"all": data}
                save_xml(adjusted_data, output_file)
            else:
                messagebox.showerror("Error", "Only .json, .yaml/.yml, and .xml formats are supported.")
                return
            
            messagebox.showinfo("Success", f"Data successfully saved to {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert data: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataConverter(root)
    root.mainloop()
