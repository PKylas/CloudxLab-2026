#! /usr/bin/python

import os
from openai import OpenAI
import glob
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from chromadb import Search, K, Knn

with open("/Users/prabhakylas/Documents/.openaikey", "r") as file:
    openai_key=file.read()

os.environ["OPENAI_API_KEY"] = openai_key

client = OpenAI()

chroma_client = chromadb.Client()

BASE_PROMPT_TEMPLATE = """
Answer the user's question.

You can do one of the following things only:

1. Answer the user's question:
ANSWER: <answer>

2. Ask user a clarification question:
ASKUSER: <question>

3. Read a file:
READFILE: <filename.docx>

4. List files/directory in a directory
LISTDIR: <directory Name>

Important:
- Output only one line.
- Do not explain.
- Do not use any format other than ANSWER, ASKUSER, or READFILE.

User's Question: {user_question}

Here is the list of documents:
{relevant_info}

The directory that contains all files: {folder}
"""


def word_doc_bits(folder_path: str) -> dict[str, str]:
    doc_pattern = os.path.join(folder_path, "*.txt")
    txt_files = glob.glob(doc_pattern)

    print(f"Found {len(txt_files)} text documents to process.")
    for file_path in txt_files:
        file_name = os.path.basename(file_path)
        print(f"Processing: {file_name}...")
        abs_file_path = os.path.join(folder_path, file_name)
        with open(abs_file_path) as file:
            data = file.read()
    
    
    
# Split the text into manageable chunks
    text_splitter = RecursiveCharacterTextSplitter(
          chunk_size=500,       # Number of characters per chunk
          chunk_overlap=200      # Overlap between chunks to keep context
         )
    data_chunks = text_splitter.create_documents([data])
    print(f"Total chunks created: {len(data_chunks)}")
    
    valid_texts = [str(text) for text in data_chunks if text]
    
    insert_chunks(valid_texts)

collection_name = "harness_collection"
try:
    collection = chroma_client.create_collection(
        name=collection_name,
        embedding_function=OpenAIEmbeddingFunction(
    ))
except Exception as e:
    collection = chroma_client.get_connection(name=collection_name)

def get_openai_embedding(text):
    if isinstance(text, str):
        response = client.embeddings.create(model="text-embedding-3-small", input=text)
        embedding = response.data[0].embedding
    return embedding

def insert_chunks(in_text):
    for i, text in enumerate(in_text):
          embedded = get_openai_embedding(text)
          collection.add(
           ids = f"id_{i}",
           embeddings = embedded,
           documents = text
         )

def search(query, top_k):
    # query_embed = get_openai_embedding(query)

    result = collection.query(

        query_texts = [query],
        n_results=top_k

    )
    for id, document in zip(result["ids"], result["documents"]):
         return (id, document) 

def call_llm(prompt: str, model: str = "o4-mini") -> str:
    response = client.responses.create(
        model=model,
        input=prompt,
    )
    return response.output_text.strip()

def summarize_context(context):
    prmt = f'''
          summary the context: {context}'''
    return prmt

def parse_action(response: str):
    response = response.strip()

    if response.startswith("ANSWER:"):
        return "ANSWER", response[len("ANSWER:"):].strip()

    if response.startswith("ASKUSER:"):
        return "ASKUSER", response[len("ASKUSER:"):].strip()

    if response.startswith("READFILE:"):
        return "READFILE", response[len("READFILE:"):].strip()
    if response.startswith("LISTDIR:"):
        return "LISTDIR", os.listdir(response[len("LISTDIR:"):].strip())

def read_file(file_name):
    return open(file_name).read()

def agent_harness(user_question: str,  max_steps = 20):
    context = ""
    max_prompt_size = 1024
    for step in range(max_steps):
        print(f"Step {step}")
        prompt = BASE_PROMPT_TEMPLATE.format(
            folder = documents_folder,
            user_question=user_question,   
            relevant_info = search(user_question, 1), # document_list could be very big, shorten by using RAG
        )
        if context:
            if len(context) > .8 * max_prompt_size:
                context = summarize_context(context)

        prompt += context
        
        print(f"Prompt: {prompt}")
        
        llm_out = call_llm(prompt)
        
        print(llm_out)
        
        action, value = parse_action(llm_out)
        
        if action == "ANSWER":
            return value

        elif action == "ASKUSER":
            user_reply = input(f"{value}\nUser: ")
            context += f"\nThe agent asked: {value}"
            context += f"\nThe user replied: {user_reply}"

        elif action == "READFILE":
            filename = value.strip()

            try:
                content_file = read_file(file_name=filename) # split the files

                context += f"\nContent of {filename}:\n{content_file}"
            except:                
                context += f"\nError: {filename} does not exist."

        else:
            context += f"""The previous LLM output was invalid:{value}
            Please respond with exactly one of:
            ANSWER: ...
            ASKUSER: ...
            READFILE: filename.txt
            """
    

if __name__ == "__main__":   
    documents_folder = "/Users/prabhakylas/Documents/CloudxLab-2026/hdfc_insurance/text_files"
    word_doc_bits(documents_folder)
     # for doc in word_bits:
     #       print(f"Type: {doc.metadata.get('category')}")
     #       print(f"Content: {doc.page_content}\n" + "-"*20)
        
    while True:
        print(" I am an insurance customer service agent! How may I help you?")
        question = input("Question: ")

        answer = agent_harness(user_question=question)  
          
        print("\nFINAL ANSWER:")
        print(answer)