import numpy as np
from tqdm import tqdm
import sys 


def read_input():
    with open("taskD/kinopoisk_input.txt", "r") as input_file:
        n, m, q = map(int, input_file.readline().split())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input_file.readline().split())))
        queries = []
        for _ in range(q):
            queries.append(input_file.readline().split())
    return n, m, q, np.array(matrix), queries


def find_closest_item(item_index, items_similarity_matrix):
    return np.argsort(items_similarity_matrix[item_index])[0]


def find_closest_user(user_index, user_similarity_matrix):
    return np.argsort(user_similarity_matrix[user_index])[1]

def recommend_movies(user_id, matrix, k=1):
    movies = list(matrix[user_id])
    indexes = []
    max_val = max(movies)
    if max_val == 0: return -2
    for i in range(len(movies)):
        if movies[i] == max_val:
            return i
    return -2


def save_results(responses):
    with open("kinopoisk_output.txt", "w") as output_file:
        output_file.write(str(len(responses)) + "\n")
        for response in responses:
            output_file.write(str(response + 1) + "\n")


def build_user_similarity_matrix(matrix, n):
    user_similarity_matrix = np.zeros((n, n))
    for i in tqdm(range(n), desc="Building user similarity matrix"):
        for j in range(i + 1, n):
            user_similarity_matrix[i, j] = np.linalg.norm(matrix[i] - matrix[j])
            user_similarity_matrix[j, i] = user_similarity_matrix[i, j]
    for i in range(n):
        user_similarity_matrix[i, i] = float('inf')
    return list(user_similarity_matrix)


def build_item_similarity_matrix(matrix, m):
    matrix_t = matrix.T
    item_similarity_matrix = np.zeros((m, m))
    for i in tqdm(range(m), desc="Building item similarity matrix"):
        for j in range(i + 1, m):
            item_similarity_matrix[i, j] = np.linalg.norm(matrix_t[i] - matrix_t[j])
            item_similarity_matrix[j, i] = item_similarity_matrix[i, j]
    for i in range(m):
        item_similarity_matrix[i, i] = float('inf')  # ensure that the similarity of an item with itself is 0.0
    return list(item_similarity_matrix)


def main():
    n, m, q, matrix, queries = read_input()
    user_similarity_matrix = build_user_similarity_matrix(matrix, n)
    items_similarity_matrix = build_item_similarity_matrix(matrix, m)
    responses = []
    for query in tqdm(queries, desc="Processing queries"):
        type, id = query
        if type == 'u':
            closest_user_id = find_closest_user(int(id) - 1, user_similarity_matrix)
            responses.append(recommend_movies(closest_user_id, matrix, k=1))
        else:
            responses.append(find_closest_item(int(id) - 1, items_similarity_matrix))
    save_results(responses)


if __name__ == "__main__":
    main()