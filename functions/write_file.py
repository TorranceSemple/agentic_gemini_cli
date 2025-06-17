import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(file_path)
    
    if not os.path.isabs(file_path):
        target_file = os.path.abspath(os.path.join(working_directory, file_path))
    else:
        target_file = os.path.abspath(file_path)
        
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    try:
        dir_path = os.path.dirname(target_file)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        with open(target_file, "w", encoding="utf-8") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return f"Error writing file: {e}"