import os
from google.genai import types

MAX_CHARS = 10000

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            # After reading the first MAX_CHARS...
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_content_string
    except Exception as e:
        return f"Error: {str(e)}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists the contents of a specified file inside the working directory, stopping after a maximum ammount of characters.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path of the file we want to print the contents of",
            ),
        },
        required=["file_path"]
    ),
)
    