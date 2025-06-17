import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    
    if not os.path.isabs(file_path):
        target_file = os.path.abspath(os.path.join(working_directory, file_path))
    else:
        target_file = os.path.abspath(file_path)
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside'
    
    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found'
    
    if not target_file.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(["python3",target_file],timeout=30,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        print(f"stdout: {result.stdout}")
        print(f"stderr: {result.stderr}")
        if result.returncode != 0:
            return f"Process exited with code {result.returncode}"
        if not result.stdout:
            return "No output produced"
               
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    
    