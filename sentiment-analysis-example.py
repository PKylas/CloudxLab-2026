#! /usr/bin/python3
from openai import OpenAI
import os
from sklearn.decomposition import PCA
import matplotlib
import matplotlib.pyplot as plt



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

def visualize_pca_2d(embeddings, words):
    pca_2d = PCA(n_components=2)
    embeddings_2d = pca_2d.fit_transform(embeddings)

    # Create a 2D scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], marker='o')
    for i, word in enumerate(words):
        plt.annotate(word, (embeddings_2d[i, 0], embeddings_2d[i, 1]))

    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.title("2D Visualization of Word Embeddings")
    plt.grid(True)
    plt.show(block=True)

# Example usage
words = ['pets', 'cat', 'pigeon', 'feline', 'kitten', 'kitten', 'fly', 'meow', 'bird']
embeddings = []
for i in words:
    embeddings.append(get_openai_embedding(i))
visualize_pca_2d(embeddings, words)