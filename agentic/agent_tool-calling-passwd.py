#! /usr/bin/python3

from openai import OpenAI
import os
import json

with open("/Users/prabhakylas/Documents/.openaikey", "r") as file:
    openai_key=file.read()

os.environ["OPENAI_API_KEY"] = openai_key

client = OpenAI()

tool1 = [
    {
        "type": "function",
        "name": "change_password",
        "description": "Take user input and change password if conditions are met.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "ssn": {
                    "type": "string",
                    "description": "A valid SSN stored in USER_DB."},
                "old_password": {
                    "type": "string",
                    "description": "For a given SSN number, an old password stored in USER_DB.",
                },
                "new_password": {
                    "type": "string",
                    "description": "The final string returned by the change_password function.",
                }
            },
            "required":["ssn", "old_password", "new_password"],
            "additionalProperties": False,
        },
    },
]

print("Tool defined!")

USER_DB = {
    "143-27-8934": {"password": "thispass!", "name": "Alice"},
    "154-36-2465": {"password": "someoldpass", "name": "Bob"},
}

print("User DB loaded with", len(USER_DB), "users.")

def change_password(ssn: str, old_password: str, new_password: str) -> str:
    c = 0
    try:
      for key, value in enumerate(USER_DB):
        if ssn is value:
            if old_password in USER_DB[value]["password"]:
                if old_password is not new_password:
                    c+=1    
                    return "Password Changed!"                  
      if c == 0:
        return "Invalid input."  
    except Exception as e:
       return f"Error: {e}"
               
    
# print(change_password("143-27-8934", "oldpass123", "newpass456"))  # Should print: Password Changed!
# print(change_password("123-45-6789", "wrongpass", "newpass456"))   # Should print: Error message
# print(change_password("000-00-0000", "anything", "anything")) 
# print(change_password('143-27-8934', 'thispass!', 'anypass4798'))
print(change_password('154-36-2465',  'someoldpass', 'pleasework@'))



system_prompt = """
You are an AI assistant that calls the change_password tool.
- The output must be the result from the change_password function."""


input_list = [
    {
        "role":"system", "content":system_prompt
    },
    {
    "role":"user", "content":"154-36-2465, someoldpass, pleasework@"
    }
]

response = client.responses.create(
    model="gpt-5.4-nano", 
    input=input_list,
    tools=tool1,
    tool_choice = "required"
    # tool_choice={"type": "function", "name": "change_password"}    
)  

input_list += response.output
pass_change = ''

# print(input_list)

print(response)

for item in response.output:
    if item.type == 'function_call' and item.name == 'change_password':
        dict_new = json.loads(item.arguments)
        in_text=dict_new['ssn']
        in_text = f"'{in_text}' "
        in_oldpass = dict_new['old_password']
        in_oldpass = f"'{in_oldpass}'"
        in_newpass = dict_new['new_password']
        in_newpass = f"'{in_newpass}'"
        pass_change = change_password(in_text, in_oldpass, in_newpass)
        input_list.append({
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": pass_change,
            })

print(input_list)
# response = client.responses.create(
#     model="gpt-4",
#     tools=tool1,
#     input = input_list
# )

# print(response.output_text)

## Tool output is wrong but the function gives the correct output:

