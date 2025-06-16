import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    sys.exit(1)

user_prompt = sys.argv[1]
response = client.models.generate_content(model='gemini-2.0-flash-001', contents=user_prompt)
messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]
prompt_tokens = response.usage_metadata.prompt_token_count
response_tokens = response.usage_metadata.candidates_token_count

if "--verbose" in sys.argv:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {prompt_tokens}\nResponse tokens: {response_tokens}")
    print(f"{response.text}")
else:
    print(f"{response.text}")