import pandas as pd
import numpy as np
from llama_index.embeddings.ollama import OllamaEmbedding
from pathlib import Path
import os


def load_data(file_path = 'taskF/Library_Input.txt'):
    books = []
    queries = []
    with open(file_path, 'r', encoding='utf-8') as file:
        n = int(file.readline().strip())
        for _ in range(n):
            books.append(file.readline().strip())
        # read the rest of the file
        m = int(file.readline().strip())
        for _ in range(m):
            queries.append(file.readline().strip())
    return n, m, books, queries

def get_query_embedding(query):
    ollama_embedding = OllamaEmbedding(
        model_name="all-minilm",
        base_url="http://localhost:11434",
        ollama_additional_kwargs={"mirostat": 0},
    )
    query_embedding = ollama_embedding.get_query_embedding(query)
    return query_embedding

def transform_banch_of_text_direct(text_batch):
    ollama_embedding = OllamaEmbedding(
        model_name="all-minilm",
        base_url="http://localhost:11434",
        ollama_additional_kwargs={"mirostat": 0},
    )
    pass_embedding = ollama_embedding.get_text_embedding_batch(
    text_batch, show_progress=True)
    return pass_embedding


def main():
    print("Loading data...", end=' ')
    n, m, books, queries = load_data()
    print('Done!')
    emb_books = transform_banch_of_text_direct(books)
    # save embeddings with original book names for future use
    book_embeddings = pd.DataFrame(emb_books, index=books)
    book_embeddings.to_pickle('book_embeddings.pkl')
    print('Book embeddings saved.')

    emb_queries = transform_banch_of_text_direct(queries)
    # save embeddings with original query names for future use
    query_embeddings = pd.DataFrame(emb_queries, index=queries)
    query_embeddings.to_pickle('query_embeddings.pkl')
    print('Query embeddings saved.')

if __name__ == "__main__":
    main()
