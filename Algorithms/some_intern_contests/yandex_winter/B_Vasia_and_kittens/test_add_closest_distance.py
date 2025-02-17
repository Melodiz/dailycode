from bisect import bisect_left
import random

def add_closest_distances(places, taken):
    taken.sort()
    m = len(places)
    k = len(taken)
    places_modif = [(x, float('inf')) for x in places]
    taken_index = 0
    
    # Forward pass
    last_taken = -float('inf')
    for i in range(m):
        if taken_index < k and places[i] == taken[taken_index]:
            places_modif[i] = (places[i], 0)
            last_taken = places[i]
            taken_index += 1
        else:
            places_modif[i] = (places[i], min(places_modif[i][1], places[i] - last_taken))
    
    # Backward pass
    taken_index = k - 1
    last_taken = float('inf')
    for i in range(m - 1, -1, -1):
        if taken_index >= 0 and places[i] == taken[taken_index]:
            places_modif[i] = (places[i], 0)
            last_taken = places[i]
            taken_index -= 1
        else:
            places_modif[i] = (places_modif[i][0], min(places_modif[i][1], last_taken - places[i]))
    
    return places_modif

def brute_force_closest_distances(places, taken):
    return [(place, min(abs(place - t) for t in taken)) for place in places]

def generate_test_case(max_m=40, max_coordinate=1000):
    m = random.randint(2, max_m)
    k = random.randint(1, m)
    
    places = sorted(random.sample(range(1, max_coordinate + 1), m))
    taken = random.sample(places, k) if k > 0 else []
    
    return places, taken

def run_tests(num_tests=500):
    for i in range(num_tests):
        places, taken = generate_test_case()
        
        optimized_result = add_closest_distances(places, taken)
        brute_force_result = brute_force_closest_distances(places, taken)
        
        print(f"Test case {i + 1}:")
        print(f"places={places}")
        print(f"taken={taken}")
        print(f"Optimized result: {optimized_result}")
        print(f"Brute-force result: {brute_force_result}")
        
        if optimized_result != brute_force_result:
            print("Test case FAILED!")
            return False
        
        print("Test case passed")
        print()
    
    print("All tests passed!")
    return True

if __name__ == "__main__":
    if run_tests():
        print("All random tests passed. The add_closest_distances function appears to be correct.")
    else:
        print("The add_closest_distances function failed on a random test case.")