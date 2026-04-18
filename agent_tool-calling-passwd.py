#! /usr/bin/python3

from openai import OpenAI
import os
import json
import hashlib

with open("/Users/prabhakylas/Documents/.openaikey", "r") as file:
    openai_key=file.read()

os.environ["OPENAI_API_KEY"] = openai_key

client = OpenAI()

USER_DB = {
    "123-45-6789": {"password": "oldpass123", "name": "Alice"},
    "987-65-4321": {"password": "securepass!", "name": "Bob"},
}

print("User DB loaded with", len(USER_DB), "users.")

def change_password(ssn: str, old_password: str, new_password: str) -> str:
    try:
        for key in USER_DB:
            if ssn is key:
              if old_password in USER_DB[key]["password"]:
                if old_password is not new_password:
                    return "Password Changed!"
            else:
                return "Incorrect input"
    except Exception as e:
        return f"Error: {e}"

# print(change_password("123-45-6789", "oldpass123", "newpass456"))  # Should print: Password Changed!
# print(change_password("123-45-6789", "wrongpass", "newpass456"))   # Should print: Error message
# print(change_password("000-00-0000", "anything", "anything")) 

tools = [
    {
        "type": "function",
        "name": "change_password",
        "description": "Take a string and hash it.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "ssn": {
                    "type": "string",
                    "description": "A valid string",
                },
                "old_password": {
                    "type": "string",
                    "description": "A valid string",
                },
                "new_password": {
                    "type": "string",
                    "description": "A valid string",
                }
            },
            "required": [["ssn"], ["old_password"], ["new_password"]],
            "additionalProperties": False,
        },
    },
]

print("Tool defined!")

input_list = [{
    "role":"user", "content":"123-45-6789"
},
{
    "role":"user", "content":"oldpass123"
},
{
    "role":"user", "content":"newpass456"
}
]

response = client.responses.create(
    model="o4-mini",
    input=input_list,
    tools=tools,
    tool_choice={"type": "function", "name": "change_password"}
)  

input_list=[]

input_list += response.output
hashed_out =''

for item in response.output:
    if item.type == 'function_call' and item.name == 'change_password':
        in_text = json.loads(item.arguments)["ssn"]
        in_oldpass = json.loads(item.arguments)["old_password"]
        in_newpass = json.loads(item.arguments)["newpassword"]
        pass_change = change_password(in_text, in_oldpass, in_newpass)
        input_list.append({
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": pass_change,
            })
    
response = client.responses.create(
    model="o4-mini",
    tools=tools,
    input=input_list,
)

print(response.output_text)

## Getting error:

##  raise self._make_status_error_from_response(err.response) from None
## openai.BadRequestError: Error code: 400 - {'error': {'message': "Invalid schema for function 'change_password': ['ssn'] is not of type 'string'.", 'type': 'invalid_request_error', 'param': 'tools[0].parameters', 'code': 'invalid_function_parameters'}}
