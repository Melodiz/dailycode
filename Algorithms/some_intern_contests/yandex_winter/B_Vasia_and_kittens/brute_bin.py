def determine_upper_bound(places, n, taken_places):
    min_distance = float('inf')
    for i in range(n-1):
        min_distance = min(min_distance, places[i+1] - places[i])
    return min_distance

def check(places, n, window_size, taken_places):
    taken_places = set(taken_places)
    
    # Initialize variables
    cats_placed = len(taken_places)
    last_placed = float('-inf')
    
    # Iterate through all places
    for i, place in enumerate(places):
        # If the place is already taken, update last_placed
        if place in taken_places:
            last_placed = place
            continue
        
        # Check distance from the last placed cat
        if place - last_placed < window_size:
            continue
        
        # Check distance to the next taken place (if exists)
        next_taken = next((p for p in places[i+1:] if p in taken_places), float('inf'))
        if next_taken - place < window_size:
            continue
        
        # If we reach here, we can place a cat
        cats_placed += 1
        last_placed = place
        
        # If we've placed all cats, return True
        if cats_placed == n:
            return True
    
    # If we couldn't place all cats, return False
    return False

def find_max_window_size(places, n, taken_places):
    # Sort all places
    all_places = sorted(set(places))
    
    # Define binary search range
    left = 0
    right = determine_upper_bound(places, n, taken_places)  if len(taken_places) > 0 else all_places[-1] - all_places[0]  # Upper bound for window size
    while left <= right:
        mid = (left + right) // 2
        if check(all_places, n, mid, taken_places):
            # If it's possible with this window size, try a larger one
            left = mid + 1
        else:
            # If it's not possible, try a smaller window size
            right = mid - 1
    
    # The maximum window size is the last successful check
    return right

def main():
    n, m, k = map(int, input().split())
    places = list(map(int, input().split()))
    if k != 0:
        taken_places = list(map(int, input().split()))
        print(find_max_window_size(places, n, taken_places))
    else:
        print(find_max_window_size(places, n, []))

    return 0

if __name__ == "__main__":
    main()