#! /usr/bin/python3
from openai import OpenAI
import os

with open("/Users/prabhakylas/Documents/.openaikey", "r") as file:
    openai_key = file.read()

os.environ["OPENAI_API_KEY"] = openai_key

client = OpenAI()

def get_openai_embedding(prompt, model="text-embedding-3-small"):
    try:
        response = client.embeddings.create(
            model=model,
            input=prompt
        )
        return response.data[0].embedding
    except Exception as e:
        print("Error fetching embedding:", e)

# Example usage
if __name__ == "__main__":
    text = "The quick brown fox jumps over the lazy dog."
    embedding = get_openai_embedding(text)
    if embedding:
        print(f"Embedding length: {len(embedding)}")
        print(embedding[:10])