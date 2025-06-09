import math

def solve_coin_ordering(coin_data):
    """
    Orders the coins based on the posterior mean estimate of their probabilities.

    Parameters:
    coin_data (list of lists): Each sublist contains [k_i, m_i] for the i-th coin.

    Returns:
    list: The indices of the coins sorted in ascending order of estimated p_i.
    """
    n = len(coin_data)
    # Calculate the posterior mean estimate for each coin
    estimates = []
    for i in range(n):
        k_i, m_i = coin_data[i]
        p_estimate = (m_i + 1) / (k_i + 2)
        estimates.append((p_estimate, i))  # Store estimate and original index
    
    # Sort the coins based on their estimates
    estimates.sort()  # Sorts by the first element of the tuple (p_estimate)
    
    # Extract the indices in the sorted order
    ordering = [index for (p_est, index) in estimates]
    
    return ordering

def main():
    data = []
    with open('coins.in', 'r') as file:
        n = int(file.readline())
        for _ in range(n):
            k_i, m_i = map(int, file.readline().split())
            data.append([k_i, m_i])

    sorted_indices = solve_coin_ordering(data)
    with open('coins.out', 'w') as file:
        file.write('\n'.join(map(str, sorted_indices)))

if __name__ == '__main__':
    main()