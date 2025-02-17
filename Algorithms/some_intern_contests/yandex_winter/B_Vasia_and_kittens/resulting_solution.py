def add_closest_distances(places, taken):
    m = len(places)
    k = len(taken)
    places_modif = [(x, float('inf')) for x in places]
    if k == 0: 
        return places_modif, abs(places[-1]-places[0])
    taken_index = 0

    # Forward pass
    last_taken = -float('inf')
    for i in range(m):
        if taken_index < k and places[i] == taken[taken_index]:
            places_modif[i] = (places[i], 0)
            last_taken = places[i]
            taken_index += 1
        else:
            places_modif[i] = (places[i], min(
                places_modif[i][1], places[i] - last_taken))

    # Backward pass
    absolute_min_distance = abs(places[-1] - places[0])
    taken_index = k - 1
    last_taken = float('inf')
    for i in range(m - 1, -1, -1):
        if taken_index >= 0 and places[i] == taken[taken_index]:
            places_modif[i] = (places[i], 0)
            last_taken = places[i]
            taken_index -= 1
        else:
            places_modif[i] = (places_modif[i][0], min(
                places_modif[i][1], last_taken - places[i]))
            
    for i in range(len(taken)-1):
        absolute_min_distance = min(absolute_min_distance, abs(taken[i] - taken[i+1]))

    return places_modif, absolute_min_distance


def check(n, m, precalc_places, window_size):
    count = 0
    left_placed = -float('inf')
    for i in range(m):
        if count == n:
            return True
        # distance to the next taken place
        if (precalc_places[i][1] < window_size) or (abs(precalc_places[i][0] - left_placed) < window_size):
            continue
        left_placed = precalc_places[i][0]
        count += 1
    return True if count >= n else False


def solve(n, m, k, places, taken):
    places.sort()
    taken.sort()
    precalc_places, right = add_closest_distances(places, taken)
    left = 0
    result = left  # Initialize result to store the last valid mid
    while left <= right:
        mid = (left + right) // 2
        if check(n-k, m, precalc_places, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result  # Return the last valid mid


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    beds = list(map(int, input().split()))
    occupied = list(map(int, input().split())) if k > 0 else []
    print(solve(n, m, k, beds, occupied))

