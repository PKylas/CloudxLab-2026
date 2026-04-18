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
    