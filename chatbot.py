#! /usr/bin/python3

from openai import OpenAI
import os


with open("/Users/prabhakylas/Documents/.openaikey", "r") as file:
    openai_key=file.read()

os.environ["OPENAI_API_KEY"]=openai_key

client = OpenAI()

system_prompt = """You answer the user's questions in the spirit of a sarcastic customer service executive:"""

class Chatbot:
    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": system_prompt,
            }
        ]
        self.total_input_tokens=0
        self.total_output_tokens=0
        self.total_tokens=0

    def ask_bot(self, question):
        self.messages.append({"role":"user", "content":question})

        responses = client.chat.completions.create(
            model="gpt-4.1",
            messages = self.messages
        )
        answer = responses.choices[0].message.content

        self.messages.append({"role":"assistant", "content":answer})

        self.total_input_tokens+=responses.usage.prompt_tokens
        self.total_output_tokens+=responses.usage.completion_tokens
        self.total_tokens+=responses.usage.total_tokens

        print("=== Token usage === \n")
        print(f"Input tokens: {self.total_input_tokens}")
        print(f"Output tokens: {self.total_output_tokens}")
        print(f"Total tokens: {self.total_tokens}\n")

        # print(responses)
        return answer

def main():
    chat = Chatbot()
    print("Chatbot started. Type 'exit' to quit.\n")

    while True:
        user_input = input("You:")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("May the fourth be with you.\n")

            print("===Token usage=== \n")
            print(f"Input tokens: {chat.total_input_tokens}")
            print(f"Output tokens: {chat.total_output_tokens}")
            print(f"Total tokens: {chat.total_tokens}")

            break
        

        answer = chat.ask_bot(user_input)
        print(f"Bot: {answer} \n")

if __name__ == "__main__":
    main()


        
