import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        print(f'Success: "{directory}" is within the working directory')

        item_data = []
        for item in os.listdir(target_dir):
            item_data.append(f"- {item}: file_size={os.path.getsize(target_dir+'/'+item)} bytes, is_dir={os.path.isdir(target_dir+'/'+item)}")

        return '\n'.join(item_data)
    except:
        return "Error"

    