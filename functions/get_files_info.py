import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    absoluste_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(absoluste_path, directory))

    valid_target_dir = os.path.commonpath(absoluste_path, target_dir) == absoluste_path

    if valid_target_dir == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if 
