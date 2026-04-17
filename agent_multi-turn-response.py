#! /usr/bin/python3

from openai import OpenAI
import os
import json

with open("/Users/prabhakylas/Documents/.openaikey", "r") as file:
    openai_key = file.read()

os.environ["OPENAI_API_KEY"] = openai_key

client = OpenAI()

context=[
    {
        "role":"system", "content":"You are a helpful assistant."
    },
    {
        "role":"user", "content":"Hello!"
    }
]

conversation_history = []

def user_chat(usr_message):
    global conversation_history
    conversation_history+=[{
        "role":"system", "content":"You are a helpful assistant."
    }, {"role":"user", "content":usr_message}]

    res = client.responses.create(
    model="o4-mini",
    input=conversation_history

    )

    reply = res.output

    answer = res.output_text
    
    conversation_history+=reply

    return answer

print(user_chat("Hi, I'm Sara!"))

print(user_chat("What was my name?"))