from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('OPEN_API_KEY')

def sike_response(prompt):
    response = openai.Completion.create(
        model = "gpt-3.5-turbo-instruct",
        prompt = prompt,
        max_tokens = 500,
        temperature=1
    )

    response_dict = response.get("choices")
    if response_dict and len(response_dict)>0:
        prompt_response = response_dict[0]['text']
    return prompt_response