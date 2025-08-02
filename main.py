import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

model = 'gemini-2.0-flash-001'


def main():
    response = ""
    # Command Line prompt
    contents = sys.argv[1:]
    
    response = client.models.generate_content(model=model, contents=contents)
    print(response.text)
    print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
    print("Response tokens: " + str(response.usage_metadata.candidates_token_count))


if __name__ == "__main__":
    main()
