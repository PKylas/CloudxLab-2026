#! /usr/bin/python3
from openai import OpenAI
import os
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import kagglehub

path = "~/Documents/Datasets/ElectronicsData.csv"
df = pd.read_csv(path)

##Combine selected five columns from the original dataset into a Dataframe
df['combined'] = (df['Sub Category'] + '.'+ df['Price'].astype(str)+ '.'+ df['Discount'].astype(str) +'.'+ df['Title'])

#convert the new dataframe into a list
text_embedding = df['combined'].tolist()

##print(df['combined'].iloc[0])

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

def calculate_distance(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.sum((a-b)**2)

# generate embeddings for the dataframe
embeddings = []
for i in text_embedding[:644]:
    embeddings.append(get_openai_embedding(i))
embeddings_np = np.array(embeddings)

#generate embedding for the search query
def search_product(query_new, k=4):
    query_embeddings = get_openai_embedding(query_new)
    result=[]
    for i, value in enumerate(embeddings_np):
        result.append((calculate_distance(value, query_embeddings), i))

    result.sort()
    top_result = result[:k]
    
    for distance, id in top_result:
        print(df.iloc[id]["Title"], "\n")

search_product("Musical instruments below price 500")