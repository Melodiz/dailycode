import functools

def solve_coin_ordering(coin_data_list):
    """
    Orders coins based on their estimated probability of heads (p_i).

    The estimation uses a Bayesian approach with a uniform prior (Beta(1,1))
    for p_i. The posterior mean E[p_i | m_i, k_i] = (m_i + 1) / (k_i + 2)
    is used as the primary sorting score.

    Refined tie-breaking rules are applied:
    - If scores are equal and score == 0.5, tie-break by original index (ascending).
    - If scores are equal and score > 0.5, tie-break by k_i (ascending), then by original index.
    - If scores are equal and score < 0.5, tie-break by k_i (descending), then by original index.

    Args:
        coin_data_list: A list of lists, where each inner list is [k_i, m_i].
                        k_i is the number of tosses for coin i.
                        m_i is the number of heads for coin i.
                        The index of the inner list corresponds to the original 0-indexed coin index.

    Returns:
        A list of integers, representing the 0-indexed original coin indices
        sorted according to the described criteria (ascending estimated p_i).
    """

    processed_coins = []
    for original_idx, data in enumerate(coin_data_list):
        k_i = data[0]
        m_i = data[1]

        # Calculate the Bayesian posterior mean score
        # Ensure floating point division
        score = (m_i + 1.0) / (k_i + 2.0)
        
        processed_coins.append({'score': score, 'k': k_i, 'original_index': original_idx})

    # Define the custom comparison function for sorting
    # This can be a nested function or a static method if part of a class
    def compare_coins_logic(item1_data, item2_data):
        s1 = item1_data['score']
        k1 = item1_data['k']
        idx1 = item1_data['original_index']

        s2 = item2_data['score']
        k2 = item2_data['k']
        idx2 = item2_data['original_index']

        # Primary sort by score
        if s1 < s2:
            return -1
        if s1 > s2:
            return 1

        # Scores are equal (s1 == s2), apply tie-breaking rules
        epsilon = 1e-9  # For floating point comparisons against 0.5

        if abs(s1 - 0.5) < epsilon:  # Score is approximately 0.5
            # Tie-break by original index (ascending)
            if idx1 < idx2:
                return -1
            if idx1 > idx2:
                return 1
            return 0
        elif s1 > 0.5:  # Score > 0.5
            # Tie-break by k ascending (smaller k first)
            if k1 < k2:
                return -1
            if k1 > k2:
                return 1
            # If k's are also tied, tie-break by original index (ascending)
            if idx1 < idx2:
                return -1
            if idx1 > idx2:
                return 1
            return 0
        else:  # Score < 0.5
            # Tie-break by k descending (larger k first)
            if k1 > k2: # item1 (with k1) comes before item2 (with k2) if k1 > k2
                return -1
            if k1 < k2: # k1 is smaller, so item2 comes before item1
                return 1
            # If k's are also tied, tie-break by original index (ascending)
            if idx1 < idx2:
                return -1
            if idx1 > idx2:
                return 1
            return 0

    # Sort the processed_coins list using the custom comparison function
    # functools.cmp_to_key is used to adapt a cmp=style function for key= argument
    processed_coins.sort(key=functools.cmp_to_key(compare_coins_logic))

    # Extract the original indices from the sorted list
    sorted_indices = [item['original_index'] for item in processed_coins]

    return sorted_indices