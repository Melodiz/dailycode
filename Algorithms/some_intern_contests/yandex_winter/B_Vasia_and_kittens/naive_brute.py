from itertools import combinations

def can_place_entities_naive(n, bed_coords, occupied_beds, min_dist):
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

def naive_brute_force(bed_coordinates, n, occupied_beds):
    for val in range(101, -1, -1):
        if can_place_entities_naive(n-len(occupied_beds), bed_coordinates, occupied_beds, val):
            return val
    return -1

def solve(n, m, k, bed_coordinates, occupied_beds):
    return naive_brute_force(bed_coordinates, n, occupied_beds)

# Main function to handle input and output
def main():
    # Read input
    n, m, k = map(int, input().split())
    bed_coordinates = list(map(int, input().split()))
    occupied_beds = list(map(int, input().split())) if k > 0 else []
    
    # Solve and print the result
    result = solve(n, m, k, bed_coordinates, occupied_beds)
    print(result)

if __name__ == "__main__":
    main()