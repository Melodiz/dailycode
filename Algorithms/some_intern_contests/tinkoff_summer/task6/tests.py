import random
import time
from tqdm import tqdm
import heapq

# Brute force solution
def brute_force(heights):
    """
    Brute force solution to find the maximum sum of height differences.
    
    Args:
        heights: List of integers representing heights of people
    
    Returns:
        Maximum possible sum of absolute differences
    """
    # Base cases
    if len(heights) <= 1:
        return 0
    
    if len(heights) == 2:
        return abs(heights[0] - heights[1])
    
    max_sum = 0
    
    # Try removing each adjacent pair and recursively solve for the remaining array
    for i in range(len(heights) - 1):
        # Calculate the difference between adjacent heights
        diff = abs(heights[i] - heights[i + 1])
        
        # Create a new array without the pair at positions i and i+1
        new_heights = heights[:i] + heights[i+2:]
        
        # Recursively find the maximum sum for the remaining people
        remaining_sum = brute_force(new_heights)
        
        # Update the maximum sum if this choice leads to a better result
        max_sum = max(max_sum, diff + remaining_sum)
    
    return max_sum


def smart(n, a):
    if n == 1:
        print(0)
        exit()

    prev = [-1] * n
    next_node = [-1] * n
    active = [True] * n

    for i in range(n):
        if i > 0:
            prev[i] = i - 1
        if i < n - 1:
            next_node[i] = i + 1

    heap = []
    for i in range(n - 1):
        diff = abs(a[i] - a[i + 1])
        heapq.heappush(heap, (-diff, i, i + 1))

    total = 0

    while heap:
        current_diff_neg, i, j = heapq.heappop(heap)
        current_diff = -current_diff_neg

        if active[i] and active[j] and next_node[i] == j and prev[j] == i:
            total += current_diff
            active[i] = False
            active[j] = False

            left_prev = prev[i]
            right_next = next_node[j]

            if left_prev != -1:
                next_node[left_prev] = right_next
            if right_next != -1:
                prev[right_next] = left_prev

            if left_prev != -1 and right_next != -1:
                new_diff = abs(a[left_prev] - a[right_next])
                heapq.heappush(heap, (-new_diff, left_prev, right_next))

    return total

def generate_test_case(n, max_val=10**9):
    """Generate a random test case with n elements"""
    return [random.randint(1, max_val) for _ in range(n)]

def run_tests(num_tests=100, max_n=300, max_val=100):
    """Run multiple tests and compare solutions"""
    for test_num in tqdm(range(1, num_tests + 1)):
        # Generate random test case
        n = random.randint(2, max_n)
        heights = generate_test_case(n, max_val)
        
        # Run both solutions
        start_time = time.time()
        brute_force_result = brute_force(heights)
        brute_force_time = time.time() - start_time
        
        start_time = time.time()
        smart_result = smart(n, heights)
        smart_time = time.time() - start_time
        
        # Compare results
        if smart_result == brute_force_result:
            result = "PASS"
        else:
            result = "FAIL"
            
        print(f"Test #{test_num}: {result} | n={n} | Smart: {smart_result} ({smart_time:.6f}s) | Brute Force: {brute_force_result} ({brute_force_time:.6f}s)")
        
        if result == "FAIL":
            print(f"Input array: {heights}")
            print("This is a failing test case!")
            return False
    
    print(f"All {num_tests} tests passed!")
    return True

if __name__ == "__main__":
    print("\nTesting random cases...")
    run_tests(num_tests=100, max_n=8, max_val=100)