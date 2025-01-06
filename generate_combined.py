"""
generate_combined.py

This script combines the contents of a boilerplate file (`boilerplate.py`) with all `.py` files
in the current directory (excluding itself and the output file), dynamically detects all functions 
defined in those files, and generates a single output file (`combined_script.py`). At the end of 
the combined file, it adds calls to all detected functions in sorted order.

Features:
- Combines the boilerplate file with all `.py` files, maintaining their order.
- Detects all function definitions dynamically using regex.
- Appends calls to all detected functions at the end of the combined script.
- Outputs the final result to `combined_script.py`.

File Requirements:
- The script assumes a `boilerplate.py` file exists in the directory.
- Other `.py` files are included in alphabetical order.

Usage:
Run the script in the directory containing `boilerplate.py` and other `.py` files:
    python generate_combined.py

The output file `combined_script.py` will contain:
1. The contents of `boilerplate.py`.
2. The contents of all `.py` files (excluding itself and `combined_script.py`), in alphabetical order.
3. Function calls to all detected functions, sorted alphabetically.
"""

import os
import re

# File paths
BOILERPLATE_FILE = "boilerplate.py"
OUTPUT_FILE = "combined_script.py"


def get_python_files():
    # Get all `.py` files in the directory except this script and the output file
    current_file = os.path.basename(__file__)
    python_files = [
        f for f in os.listdir()
        if f.endswith('.py') and f not in {current_file, OUTPUT_FILE}
    ]
    # Sort files alphabetically
    return sorted(python_files)


def find_functions_in_file(file_path):
    # Extract all function names defined in the file
    function_pattern = r"^def\s+(\w+)\s*\("
    functions = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                match = re.match(function_pattern, line)
                if match:
                    functions.append(match.group(1))
    except FileNotFoundError:
        print(f"Error: {file_path} not found!")
    return functions


def combine_files():
    # Read boilerplate.py content
    try:
        with open(BOILERPLATE_FILE, 'r') as boilerplate:
            boilerplate_content = boilerplate.read()
            print(f"Read boilerplate.py content successfully.")
    except FileNotFoundError:
        print(f"Error: {BOILERPLATE_FILE} not found!")
        return
    
    # Get sorted list of Python files
    python_files = get_python_files()
    
    # Read the content of all Python files and find functions
    python_contents = []
    all_function_calls = []
    for py_file in python_files:
        try:
            # Add file content to combined script
            with open(py_file, 'r') as f:
                python_contents.append(f"# --- {py_file} ---\n" + f.read())
            
            # Find callable functions in the file
            functions = find_functions_in_file(py_file)
            all_function_calls.extend(functions)
            print(f"Found functions in {py_file}: {functions}")
        except FileNotFoundError:
            print(f"Error: {py_file} not found!")
            continue
    
    # Combine the content
    combined_content = boilerplate_content + "\n\n" + "\n\n".join(python_contents)
    
    # Add calls to all functions found
    combined_content += "\n\n# Call all functions in sorted order\n"
    for func in sorted(all_function_calls):
        combined_content += f"{func}()\n"
    
    # Write to the output file
    with open(OUTPUT_FILE, 'w') as output:
        output.write(combined_content)
        print(f"Written combined content to {OUTPUT_FILE}")


if __name__ == "__main__":
    combine_files()
