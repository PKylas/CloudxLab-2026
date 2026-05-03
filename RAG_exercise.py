#! /usr/bin/python3

import os
from openai import OpenAI
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from chromadb import Search, K, Knn



chroma_client = chromadb.Client()

with open("/Users/prabhakylas/Documents/.openaikey", "r") as file:
    openai_key=file.read()

os.environ["OPENAI_API_KEY"]=openai_key

client = OpenAI()

with open("/Users/prabhakylas/Documents/CloudxLab-2026/company_polices.txt") as file:
    data = file.read()

def get_chunk(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start+chunk_size
        chunks.append(text[start:end])
        start+=chunk_size-overlap
    return chunks

in_text = get_chunk(data)

## Generate embeddings manually for all the chunks
# def get_openai_embedding(in_text, model="text-embedding-ada-002"):
#     responses = []
#     start = 0
#     length = len(in_text)
#     while (start < length):
#         try:
#             response = client.embeddings.create(
#                 model=model,
#                 input=in_text[start]
#             )
#             responses.append(response)
#             start+=1
#         except Exception as e:
#             print("Error fetching embedding:", e)

#     return responses

# embed = get_openai_embedding(in_text)
# print(len(embed))

def get_openai_embedding(query):
    response = client.embeddings.create(model="text-embedding-3-small", input=query)
    embedding = response.data[0].embedding
    return embedding

collection_name = "rag_collection"
try:
    collection = chroma_client.create_collection(
        name=collection_name,
        embedding_function=OpenAIEmbeddingFunction(
    ))
except Exception as e:
    collection = chroma_client.get_connection(name=collection_name)

def insert_chunks(data_chunk):
    #  data_stored = []
     for i, chunk in enumerate(data_chunk):
         embedded = get_openai_embedding(chunk)
        #  data_stored.append(
        #      {
        #         'id': f"id_{i}",
        #         'vector': embedded,
        #         'text': chunk 
        #      }

        #  )
         collection.add(
           ids = f"id_{i}",
           embeddings = embedded,
           documents = chunk
         )
    
insert_chunks(in_text)

def search(query, top_k):
    # query_embed = get_openai_embedding(query)

    result = collection.query(

        query_texts = [query],
        n_results=top_k

    )
    for id, document in zip(result["ids"], result["documents"]):
         return (id, document) 

def generate_answer(question, relevant_info):

    system_prompt = f"""
You are a helpful assistant.
Answer the question using ONLY the context below.
If the answer is not in the context, say: "I could not find that in the provided document."

Context:
{relevant_info}
"""
    response = client.responses.create(
        model="gpt-4.1",
        input=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question},
        ],
    )

    return response.output_text

def rag_pipeline(question):
    relevant_info = search(question, 1)
    answer = generate_answer(question, relevant_info)
    return answer

question = "what is the sick leave policy"

print(rag_pipeline(question))