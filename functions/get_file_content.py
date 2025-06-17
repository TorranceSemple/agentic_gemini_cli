import os
MAX_CHARS = 10000


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)

    if not os.path.isabs(file_path):
        target_file = os.path.abspath(os.path.join(working_directory, file_path))
    else:
        target_file = os.path.abspath(file_path)
    
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(target_file):
        return f'Error: "{file_path}" is a directory'
    if not os.path.exists(target_file):
        return f'Error: "{file_path}" does not exist'
    if not os.path.isfile(target_file):
        return f'Error: "{file_path}" is not a file'
    
    try:
        file_size = os.path.getsize(target_file)
        
        with open(target_file, "r", encoding="utf-8") as f:
            if file_size > MAX_CHARS:
                error = f' [...File "{file_path}" truncated at 10000 characters]'
                return f.read(MAX_CHARS) + error
            return f.read(MAX_CHARS)
            
    except Exception as e:
        return f"Error reading file: {e}"
    
    