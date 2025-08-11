import os


def get_files_info(working_directory, directory="."):
    abs_path = os.path.abspath(working_directory)
    rel_path = os.path.join(working_directory, directory)

    output_str = [f"Result for { "current" if directory == "." else f"\'{directory}\'"} directory:"]
    
    if directory in os.listdir(abs_path) or directory == ".":
        if os.path.isdir(rel_path):
            contents = os.listdir(rel_path)
            for content in contents:
                if ".txt" in content:
                    continue
                try:
                    c = os.path.join(rel_path, content)
                    output_str.append(f"- {content}: file_size={os.path.getsize(c)} bytes, is_dir={os.path.isdir(c)}")
                except OSError as e:
                    return f"Error: {e}"
            return "\n  ".join(output_str)
        else:
            output_str.append(f"Error: \"{directory}\" is not a directory")
            return "\n".join(output_str)
    else:
        output_str.append(f"- Error: Cannot list \"{directory}\" as it is outside the permitted working directory")
        return "\n  ".join(output_str)
