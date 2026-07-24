from openai import OpenAI
import os
import sys

with open("/Users/prabhakylas/Documents/.openaikey", "r") as file:
    openai_key=file.read()

os.environ["OPENAI_API_KEY"] = openai_key

client = OpenAI()  # reads ANTHROPIC_API_KEY from env

def honest_ask(question):
    if "internal memo" or "Q3 2024" in question:
        print("Sorry, I can't answer this question.")
        sys.exit()
    else:
      response = client.chat.completions.create(
        model="gpt-4.1",
        max_tokens=256,
        messages=[{"role": "user", "content": question}]
      )
      return response.choices[0].message.content

# print(ask("What is the capital of France?"))
# print(ask("Who wrote Hamlet?"))
# This is a made-up internal document. The model has never seen it.
print(honest_ask("According to Acme Corp's Q3 2024 internal memo, what is the new expense policy for travel?"))

