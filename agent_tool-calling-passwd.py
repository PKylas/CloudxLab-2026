#! /usr/bin/python3

from openai import OpenAI
import os
import json
import hashlib

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
    "123-45-6789": {"password": "oldpass123", "name": "Alice"},
    "987-65-4321": {"password": "securepass!", "name": "Bob"},
}

print("User DB loaded with", len(USER_DB), "users.")

def change_password(ssn: str, old_password: str, new_password: str) -> str:
    try:
        for key, value in enumerate(USER_DB):
            if ssn is value:
                if old_password in USER_DB[value]["password"]:
                    if old_password is not new_password:
                        return "Password Changed!"              
            elif key == len(USER_DB)-1:
                return "Invalid input."
    except Exception as e:
        return f"Error: {e}"

# print(change_password("123-45-6789", "oldpass123", "newpass456"))  # Should print: Password Changed!
# print(change_password("123-45-6789", "wrongpass", "newpass456"))   # Should print: Error message
# print(change_password("000-00-0000", "anything", "anything")) 
print(change_password("987-65-4321", "securepass!", "anypass4798"))


system_prompt = """
You are an AI assistant that calls the change_password tool.
- Make sure that the SSN in user input is present in the USER_DB dictionary.
- Make sure that the old password is present in the USER_DB dictionary.
- Make sure that the old passord is not the new password.
- The output must be the result from the change_password function."""

input_list = [
    {
        "role":"system", "content":system_prompt
    },
    {
    "role":"user", "content":"987-65-4321, securepass!, anypass4798"
}
]

response = client.responses.create(
    model="o4-mini", 
    input=input_list,
    tools=tool1,
    tool_choice={"type": "function", "name": "change_password"}    
)  

input_list=[]

input_list += response.output
pass_change = ''

for item in response.output:
    if item.type == 'function_call' and item.name == 'change_password':
        in_text = json.loads(item.arguments)["ssn"]
        in_oldpass = json.loads(item.arguments)["old_password"]
        in_newpass = json.loads(item.arguments)["new_password"]
        pass_change = change_password(in_text, in_oldpass, in_newpass)
        input_list.append({
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": pass_change,
            })
        
print(input_list)

response = client.responses.create(
    model="o4-mini",
    tools=tool1,
    input = input_list
)

print(response.output_text)


## Tool output is wrong but the function gives the correct output:

# Tool defined!
# User DB loaded with 2 users.
# Password Changed! --> change_password function output
# [ResponseReasoningItem(id='rs_0e2ef5515c9547610069e4dc257fc8819fad597e483d6f6da3', summary=[], type='reasoning', content=None, encrypted_content=None, status=None), \
# ResponseFunctionToolCall(arguments='{"ssn":"987-65-4321","old_password":"securepass!","new_password":"anypass4798"}', \
# call_id='call_KsKqGs1ouJbyNaJ6yhWY2GKG', name='change_password', type='function_call', id='fc_0e2ef5515c9547610069e4dc279c0c819fa2394f3135dd482e', status='completed'), \
# {'type': 'function_call_output', 'call_id': 'call_KsKqGs1ouJbyNaJ6yhWY2GKG', 'output': 'Invalid input.'}] --> wrong output
# It seems there was an issue updating your password. Please double-check your SSN and current password and try again. If the problem persists, contact support for assistance.