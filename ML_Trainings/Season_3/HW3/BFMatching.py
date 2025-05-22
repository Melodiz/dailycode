import numpy as np
# do not change the code in the block below
# __________start of block__________
class DummyMatch:
    def __init__(self, queryIdx, trainIdx, distance):
        self.queryIdx = queryIdx  # index in des1
        self.trainIdx = trainIdx  # index in des2
        self.distance = distance
# __________end of block__________


def match_key_points_numpy(des1: np.ndarray, des2: np.ndarray) -> list:
    """
    Match descriptors using brute-force matching with cross-check.

    Args:
        des1 (np.ndarray): Descriptors from image 1, shape (N1, D)
        des2 (np.ndarray): Descriptors from image 2, shape (N2, D)

    Returns:
        List[DummyMatch]: Sorted list of mutual best matches.
    """
    matches = []
    
    distances = np.sqrt(((des1[:, np.newaxis, :] - des2[np.newaxis, :, :]) ** 2).sum(axis=2))
    
    best_match_des1_to_des2 = np.argmin(distances, axis=1)
    
    best_match_des2_to_des1 = np.argmin(distances, axis=0)
    
    for i in range(len(des1)):
        j = best_match_des1_to_des2[i] 
        
        if best_match_des2_to_des1[j] == i:
            match = DummyMatch(
                queryIdx=i,
                trainIdx=j,
                distance=distances[i, j]
            )
            matches.append(match)
    
    matches.sort(key=lambda x: x.distance)
    
    return matches