import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:

        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if file_path[-3:] != '.py':
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]
        if args:
            command.extend(args)

        ran = subprocess.run(command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30)
        output, error, returncode = ran.stdout, ran.stderr, str(ran.returncode)
        
        return_string = ''
        if returncode != '0':
            return_string += f"Process exited with code {returncode}"
        
        if not output and not error:
            return_string += "No output produced"
        if output:
            return_string += f"STDOUT: {output}"
        if error:
            return_string += f"STDERR: {error}"
        
        return return_string

    except Exception as e:
        return f"Error: executing Python file: {e}"

