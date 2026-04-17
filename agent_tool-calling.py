#! /usr/bin/python3

from openai import OpenAI
import os
import json
import hashlib

with open("/Users/prabhakylas/Documents/.openaikey", "r") as file:
    openai_key=file.read()

os.environ["OPENAI_API_KEY"] = openai_key

client = OpenAI()

tools = [
    {
        "type": "function",
        "name": "generate_hash",
        "description": "Take a string and hash it.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "text_in": {
                    "type": "string",
                    "description": "A valid string",
                },
            },
            "required": ["text_in"],
            "additionalProperties": False,
        },
    },
]

print("Tool defined!")

def generate_hash(text: str) -> str:
    try:
        hash_object = hashlib.sha256()
        res = hash_object.update(text.encode('utf-8'))
        hashed = hash_object.hexdigest()
        return hashed
    except Exception as e:
        return f"Error: {e}"
# print(generate_hash("This may be a string."))

input_list = [{
    "role":"user",
    "content": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts."
} ]

response = client.responses.create(
    model="o4-mini",
    input=input_list,
    tools=tools,
    tool_choice={"type": "function", "name": "generate_hash"}
)  

input_list=[]

input_list += response.output
hashed_out =''

for item in response.output:
    if item.type == 'function_call' and item.name == 'generate_hash':
        in_text = json.loads(item.arguments)["text_in"]
        hashed_out = generate_hash(in_text)
        input_list.append({
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": hashed_out,
            })
    
response = client.responses.create(
    model="o4-mini",
    tools=tools,
    input=input_list,
)

print(response.output_text)

## First time output:

# I’ve generated a SHA-256 hash of the provided text:

# e0716264b5ca2fbf310f999ee5954053a3d6971e8689fc14b476dd798729ce37

# Let me know if you’d like anything else—summaries, translations, analyses, or other transformations! 

# The output different in subsequent runs. Please suggest how I can cache the first time response.
