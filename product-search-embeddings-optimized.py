#! /usr/bin/python3
from openai import OpenAI
import os
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import chromadb

chroma_client = chromadb.Client()

path = "~/Documents/Datasets/ElectronicsData.csv"
df = pd.read_csv(path)

df['Price_string'] = [str(i) for i in df['Price']]
df['Discount_string']=[str(i) for i in df['Discount']]
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

##print(df['Price_string'])

embeddings_sc = df['Sub Category'].apply(lambda x: model.encode(x).tolist())
embeddings_price = df['Price_string'].apply(lambda x: model.encode(x).tolist())
embeddings_discount = df['Discount_string'].apply(lambda x: model.encode(x).tolist())
embeddings_title = df['Title'].apply(lambda x: model.encode(x).tolist())

embeddings_combined = embeddings_sc + embeddings_price + embeddings_discount + embeddings_title

df['combined'] = df['Sub Category']+" "+df['Price_string']+" "+df['Discount_string']+" "+df['Title']

collection_name = "electronics_collection"
try:
    collection = chroma_client.create_collection(name=collection_name)
except Exception as e:
    # If the collection already exists
    collection = chroma_client.get_collection(name=collection_name)

document_ids = [f"id_{i}" for i in range(len(df['Title']))]


collection.add(
    documents=df['combined'].tolist(),
    ids=document_ids
)

result = collection.query( 
    query_texts=["laptops with discount"],
    n_results=5,
)

filtered_results={
    'ids':[],
    'documents':[],
    'distances':[],
}
unique_ids=set()

for i, doc_id in enumerate(result['ids'][0]):
    if doc_id not in unique_ids:
        unique_ids.add(doc_id)
        filtered_results['ids'].append(doc_id)
        filtered_results['documents'].append(result['documents'][0][i])
        filtered_results['distances'].append(result['distances'][0][i])

print(filtered_results)