import numpy as np
from sklearn.cluster import DBSCAN
from itertools import combinations


def are_colinear(p1, p2, p3, epsilon=1e-5):
    """Check if three points are colinear."""
    return abs((p2[1] - p1[1]) * (p3[0] - p1[0]) - (p3[1] - p1[1]) * (p2[0] - p1[0])) < epsilon


def slope(p1, p2):
    """Calculate slope between two points."""
    if p2[0] - p1[0] == 0:
        return float('inf')
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


def group_colinear_points(points, eps=0.1, min_samples=2):
    """Group colinear points into clusters."""
    n = len(points)
    slopes = []

    # Calculate slopes between all pairs of points
    for i, j in combinations(range(n), 2):
        slopes.append(slope(points[i], points[j]))

    # Cluster slopes using DBSCAN
    clustering = DBSCAN(eps=eps, min_samples=min_samples).fit(
        np.array(slopes).reshape(-1, 1))

    # Group points based on slope clusters
    clusters = {}
    for i, label in enumerate(clustering.labels_):
        if label == -1:
            continue
        if label not in clusters:
            clusters[label] = set()
        clusters[label].add(tuple(points[i]))

    # Verify collinearity within each cluster
    colinear_clusters = []
    for cluster in clusters.values():
        if len(cluster) < 3:
            continue
        if all(are_colinear(p1, p2, p3) for p1, p2, p3 in combinations(cluster, 3)):
            colinear_clusters.append(list(cluster))

    return colinear_clusters


# Example usage
points = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (0, 2)]
clusters = group_colinear_points(points)

print("Colinear clusters:")
for i, cluster in enumerate(clusters):
    print(f"Cluster {i + 1}: {cluster}")
