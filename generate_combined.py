import os
import re

# File paths
BOILERPLATE_FILE = "boilerplate.py"
OUTPUT_FILE = "combined_script.py"

def get_run_files():
    # Find all files starting with 'run_' and ending with .py
    all_run_files = [f for f in os.listdir() if re.match(r"run_\d+[a-d]\.py", f)]
    
    # Extract numeric part and sort by number and letter (e.g., run_1a, run_1b, etc.)
    sorted_run_files = sorted(all_run_files, key=lambda x: (int(re.search(r"run_(\d+)", x).group(1)), x[-5]))
    return sorted_run_files

def combine_files():
    # Read boilerplate.py content
    try:
        with open(BOILERPLATE_FILE, 'r') as boilerplate:
            boilerplate_content = boilerplate.read()
    except FileNotFoundError:
        print(f"Error: {BOILERPLATE_FILE} not found!")
        return

    # Get sorted list of run_* files
    run_files = get_run_files()

    # Read the content of all run_* files
    run_contents = []
    for run_file in run_files:
        try:
            with open(run_file, 'r') as f:
                run_contents.append(f"# --- {run_file} ---\n" + f.read())
        except FileNotFoundError:
            print(f"Error: {run_file} not found!")
            continue

    # Combine the content
    combined_content = boilerplate_content + "\n\n" + "\n\n".join(run_contents)

    # Write to the output file
    with open(OUTPUT_FILE, 'w') as output:
        output.write(combined_content)

    print(f"Combined script written to {OUTPUT_FILE}")

if __name__ == "__main__":
    combine_files()
