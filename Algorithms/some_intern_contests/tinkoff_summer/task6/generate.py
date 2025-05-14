import random
from solution import smart
from tqdm import tqdm

def generate_test_cases(num_cases=100, min_size=10**5, max_size=3*10**5, min_height=1, max_height=10**9):
    test_cases = []
    
    for _ in tqdm(range(num_cases)):
        # Generate random array size between min_size and max_size
        size = random.randint(min_size, max_size)
        
        # Generate random heights
        heights = [random.randint(min_height, max_height) for _ in range(size)]
        
        # Calculate expected output using brute force solution
        expected_output = smart(heights)
        
        test_cases.append((heights, expected_output))
    
    return test_cases

def write_test_cases_to_file(test_cases, filename="task6/6_casesLARGE.txt"):

    with open(filename, 'w') as f:
        for i, (heights, expected_output) in enumerate(test_cases, 1):
            f.write(f"{len(heights)}\n")
            f.write(' '.join(map(str, heights)) + '\n')
            f.write(f"{expected_output}\n")

if __name__ == "__main__":
    print("Generating 1000 test cases...")
    test_cases = generate_test_cases()
    write_test_cases_to_file(test_cases)
    print(f"Successfully generated 1000 test cases and wrote them to 6_cases.txt")