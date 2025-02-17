from itertools import combinations
from resulting_solution import check, add_closest_distances
import random
from tqdm import tqdm

def generate_test_case(max_m=20, max_coordinate=100):
    n = random.randint(2, max_m - 1)
    m = random.randint(n + 1, max_m)
    k = random.randint(0, (n - 1)//2)
    
    places = sorted(random.sample(range(1, max_coordinate + 1), m))
    taken_places = random.sample(places, k) if k > 0 else []
    
    return n, m, k, places, taken_places

def can_place_entities_naive(n, m, k, bed_coords, occupied_beds, min_dist):
    # Convert occupied beds to a set for quick lookup
    occupied_set = set(occupied_beds)
    
    # Calculate available beds by excluding occupied ones
    available_beds = [bed for bed in bed_coords if bed not in occupied_set]
    
    cats_to_place = n
    
    # Generate all combinations of placing the cats_to_place on available beds
    for combo in combinations(available_beds, cats_to_place):
        # Combine the occupied beds with the current combination
        all_cats = list(combo) + occupied_beds
        
        # Sort the positions of all cats
        all_cats.sort()
        
        # Calculate the minimum distance between any two cats
        min_distance = min(all_cats[i+1] - all_cats[i] for i in range(len(all_cats) - 1))
        
        # Check if the minimum distance is at least min_dist
        if min_distance >= min_dist:
            return True
    
    return False

def min_val(taken_places):
    min_dist = float('inf')
    for i in range(len(taken_places) - 1):
        min_dist = min(min_dist, taken_places[i + 1] - taken_places[i])
    return min_dist if min_dist!= float('inf') else 0


def test_can_place_cats(num_tests=1000):
    for test_num in range(num_tests):
        # Generate a test case
        n, m, k, places, taken = generate_test_case()
        places.sort()
        taken.sort()

        modif_places, placed_constrain = add_closest_distances(places, taken)
        
        # Generate a random minimum distance
        min_dist = random.randint(placed_constrain, max(places) - min(places))
        
        # Run both functions
        naive_result = can_place_entities_naive(n, m, k, places, taken, min_dist)
        optimized_result = check(n, m, modif_places, min_dist)
        
        # Compare results
        if naive_result != optimized_result:
            print(f"Test case {test_num + 1} failed:")
            print(f"n={n}, m={m}, k={len(taken)}")
            print(f"places={places}")
            print(f"taken={taken}")
            print(f"min_dist={min_dist}")
            print(f"Naive result: {naive_result}")
            print(f"Optimized result: {optimized_result}")
            print(f"Modified places: {modif_places}")
            return False
    
    print(f"All {num_tests} test cases passed!")
    return True

if __name__ == "__main__":
    test_can_place_cats()
