import time
import random
from resulting_solution import solve

def generate_extreme_input():
    n = 100000  # Maximum number of cats
    m = 100000  # Maximum number of beds
    k = n - 1   # Maximum number of occupied beds (n-1 to leave at least one cat to place)
    
    beds = random.sample(range(1, 1000001), m)  # Generate m unique bed coordinates
    occupied = random.sample(beds, k)  # Randomly select k beds as occupied
    
    return n, m, k, beds, occupied

def measure_time():
    print("Generating extreme input...")
    n, m, k, beds, occupied = generate_extreme_input()
    print(f"Input size: n={n}, m={m}, k={k}")

    print("\nRunning solution...")
    start_time = time.time()
    result = solve(n, m, k, beds, occupied)
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    print(f"Result: {result}")

if __name__ == "__main__":
    measure_time()