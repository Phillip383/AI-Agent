import os
from functions.config import MAX_FILE_SIZE

def get_file_content(working_directory, file_path):
    abs_path = os.path.abspath(working_directory)
    
    if file_path in os.listdir(abs_path):
        path = os.path.join(abs_path, file_path)
        
        if os.path.isfile(path):
            try:
                with open(path, "r") as file:
                    content = file.read()
                    if content.__len__() > MAX_FILE_SIZE:
                        content = content[:MAX_FILE_SIZE]
                        content += f"[\n...File \"{file_path}\" truncated at {MAX_FILE_SIZE} characters]"
                return content

            except Exception as e:
                return f"Error: {e}"
        else:
            return f"Error: File not found or is not a regular file: \"{file_path}\""
    else:
        return f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory"