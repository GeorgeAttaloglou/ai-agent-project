import os
import argparse
from prompts import system_prompt
from call_function import available_functions, call_function
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("No API key")

    parser = argparse.ArgumentParser(
        prog="uv run main.py",
        description="a simple command line chatbot in python",
    )
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    verbose = args.verbose
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
        ),
    )

    if verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if not response.function_calls:
        print(response.text)
        return

    function_results = []
    for function_call in response.function_calls:
        function_call_result = call_function(function_call, verbose)

        if not function_call_result.parts:
            raise Exception("Function Call Error (1): call_function should have a non-empty .parts list.")
        if not function_call_result.parts[0].function_response:
            raise Exception("Function Call Error (2): Empty function response list")
        if not function_call_result.parts[0].function_response.response:
            raise Exception("Function Call Error (3): Empty function response field")

        function_results.append(function_call_result.parts[0])

        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")


if __name__ == "__main__":
    main()