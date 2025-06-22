import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from tqdm import tqdm

# Load data from file
data_path = "taskC/data.txt"
file = open(data_path, 'r')
n, cost, C = list(map(int, file.readline().split()))
houses = [tuple(map(int, line.split())) for line in file]
houses_df = pd.DataFrame(houses, columns=['x', 'y'])

# Function to calculate Euclidean distance
def euclidean_distance(house, centroid):
    return np.sqrt((house['x'] - centroid['x'])**2 + (house['y'] - centroid['y'])**2)

# Function to calculate expected profit
def calculate_expected_profit(C, cost, houses_df, k):
    total_cost = 0
    for cluster in range(k):
        cluster_houses = houses_df[houses_df['cluster'] == cluster]
        for _, house in cluster_houses.iterrows():
            distance = house['distance']
            total_cost += cost * ((distance ** (1/4)) + 1) / len(cluster_houses)
    
    expected_profit = C - total_cost
    return expected_profit

max_profit = float('-inf')
optimal_k = None
optimal_centroids = None
optimal_labels = None
results = {}

# Iterate over possible values of k
for k in tqdm(range(336, 345)):
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(houses_df[['x', 'y']])
    houses_df['cluster'] = kmeans.labels_

    # Calculate centroids of clusters
    centroids = houses_df.groupby('cluster').mean()
    centroids_list = centroids[['x', 'y']].to_numpy().tolist()
    places_df = pd.DataFrame(centroids_list, columns=['x', 'y'])

    # Calculate distance between each house and its corresponding centroid
    houses_df['distance'] = houses_df.apply(
        lambda house: euclidean_distance(house, centroids.loc[house['cluster']]), axis=1)

    # Calculate total expected profit for the given k
    total_expected_profit = calculate_expected_profit(C, cost, houses_df, k)
    
    results[k] = total_expected_profit
    
    if total_expected_profit > max_profit:
        max_profit = total_expected_profit
        optimal_k = k
        optimal_centroids = centroids_list
        optimal_labels = houses_df['cluster'].tolist()

# Save results to a text file
with open('log.txt', 'w') as file:
    for k, profit in results.items():
        file.write(f'{k} {profit}\n')

# Print the results
print(f"Max Profit: {max_profit}")
print(f"Optimal k: {optimal_k}")