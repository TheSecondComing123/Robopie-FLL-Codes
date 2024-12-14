"""
generate_combined.py

This script combines the contents of a boilerplate file (`boilerplate.py`) with multiple `run_*` files
from the current directory, dynamically detects functions defined in the `run_*` files, and generates
a single output file (`combined_script.py`). At the end of the combined file, it adds calls to all 
valid functions found in the `run_*` files in sorted order.

The script handles two types of function naming conventions:
1. Functions named `run<x>()`, where `<x>` is a number (e.g., `run1()`).
2. Functions named `run<x><a/b/c/d>()`, where `<x>` is a number and `<a/b/c/d>` is an optional 
   letter suffix (e.g., `run1a()`, `run2c()`).

Features:
- Combines the boilerplate file with all `run_*` files, maintaining their order.
- Detects valid `run_*` functions dynamically using regex.
- Appends calls to all detected functions at the end of the combined script.
- Outputs the final result to `combined_script.py`.

File Requirements:
- The script assumes a `boilerplate.py` file exists in the directory.
- The `run_*` files must follow the naming pattern: `run_<number>.py` or `run_<number><a/b/c/d>.py`.

Usage:
Run the script in the directory containing `boilerplate.py` and `run_*` files:
    python generate_combined.py

The output file `combined_script.py` will contain:
1. The contents of `boilerplate.py`.
2. The contents of all `run_*` files, in sorted order.
3. Function calls to all detected `run_*` functions.

Example:
If the directory contains:
- boilerplate.py
- run_1.py (with `run_1a()` and `run_1b()`)
- run_2.py (with `run2()`)

The generated `combined_script.py` will contain:
- Contents of `boilerplate.py`
- Contents of `run_1.py` and `run_2.py`
- Calls to `run_1a()`, `run_1b()`, and `run2()` in that order.

"""

import os
import re

# File paths
BOILERPLATE_FILE = "boilerplate.py"
OUTPUT_FILE = "combined_script.py"


def get_run_files():
	# Find all files starting with 'run_' or 'run' and ending with .py
	all_run_files = [f for f in os.listdir() if re.match(r"run(_\d+[a-d]?|\d+)?\.py", f)]
	# Sort files by numeric value in the name (e.g., run_1, run_2)
	sorted_run_files = sorted(all_run_files, key=lambda x: re.search(r"(\d+)", x).group(1))
	return sorted_run_files


def find_functions_in_file(file_path):
	# Extract all function names defined in the file
	function_pattern = r"^def\s+(run\d+(?:[a-d]?)?)\s*\("
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
	
	# Get sorted list of run_* files
	run_files = get_run_files()
	
	# Read the content of all run_* files and find functions
	run_contents = []
	all_function_calls = []
	for run_file in run_files:
		try:
			# Add file content to combined script
			with open(run_file, 'r') as f:
				run_contents.append(f"# --- {run_file} ---\n" + f.read())
			
			# Find callable functions in the file
			functions = find_functions_in_file(run_file)
			all_function_calls.extend(functions)
			print(f"Found functions in {run_file}: {functions}")
		except FileNotFoundError:
			print(f"Error: {run_file} not found!")
			continue
	
	# Combine the content
	combined_content = boilerplate_content + "\n\n" + "\n\n".join(run_contents)
	
	# Add calls to all functions found
	combined_content += "\n\n# Call all functions in order\n"
	for func in all_function_calls:
		combined_content += f"{func}()\n"
	
	# Write to the output file
	with open(OUTPUT_FILE, 'w') as output:
		output.write(combined_content)
		print(f"Written combined content to {OUTPUT_FILE}")


if __name__ == "__main__":
	combine_files()
