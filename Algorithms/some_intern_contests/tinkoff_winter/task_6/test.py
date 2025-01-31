from itertools import combinations
import random
import time

def is_non_degenerate(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) != (p3[0] - p1[0]) * (p2[1] - p1[1])

def solve(n, points):
    valid_triangles = []
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if is_non_degenerate(points[i], points[j], points[k]):
                    valid_triangles.append((i, j, k))
    
    def triangle_perimeter(t):
        return sum(abs(points[t[i]][0] - points[t[j]][0]) + abs(points[t[i]][1] - points[t[j]][1]) 
                   for i, j in [(0,1), (1,2), (2,0)])
    
    valid_triangles.sort(key=triangle_perimeter, reverse=True)
    
    memo = {}
    stack = [(0, 0, 0)]  # (index, used_mask, count)
    max_count = 0

    while stack:
        index, used_mask, count = stack.pop()
        
        if count > max_count:
            max_count = count
        
        if index == len(valid_triangles):
            continue
        
        state = (index, used_mask)
        if state in memo and memo[state] >= count:
            continue
        memo[state] = count
        
        current_triangle = valid_triangles[index]
        triangle_mask = (1 << current_triangle[0]) | (1 << current_triangle[1]) | (1 << current_triangle[2])
        
        if used_mask & triangle_mask == 0:
            stack.append((index + 1, used_mask | triangle_mask, count + 1))
        
        stack.append((index + 1, used_mask, count))
    
    return max_count

def generate_random_points(n, coord_range):
    return [(random.randint(-coord_range, coord_range), random.randint(-coord_range, coord_range)) for _ in range(n)]

def test_solve_with_random_inputs(num_tests):
    MAX_N = 299
    COORD_RANGE = 10**9

    for test in range(1, num_tests + 1):
        n = random.randint(4, MAX_N)
        points = generate_random_points(n, COORD_RANGE)

        start_time = time.time()
        result = solve(n, points)
        end_time = time.time()

        print(f"Test {test}:")
        print(f"n = {n}")
        print(f"Result: {result}")
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        print()

def test_max_input():
    MAX_N = 299
    COORD_RANGE = 10**9

    points = generate_random_points(MAX_N, COORD_RANGE)

    start_time = time.time()
    result = solve(MAX_N, points)
    end_time = time.time()

    print("Maximum input test:")
    print(f"n = {MAX_N}")
    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    test_solve_with_random_inputs(5)  # Run 5 random tests
    test_max_input()  # Run test with maximum input