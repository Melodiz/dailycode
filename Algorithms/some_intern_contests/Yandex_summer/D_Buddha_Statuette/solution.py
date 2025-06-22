def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    counts = [0] * (k + 1)
    
    left = 0
    current_sum = 0
    min_cost = float('inf')
    
    types_found = 0

    for right in range(n):
        statuette_type = a[right]
        current_sum += statuette_type

        if 1 <= statuette_type <= k:
            if counts[statuette_type] == 0:
                types_found += 1
            counts[statuette_type] += 1

        while types_found == k:
            min_cost = min(min_cost, current_sum)

            statuette_to_remove = a[left]
            current_sum -= statuette_to_remove

            if 1 <= statuette_to_remove <= k:
                counts[statuette_to_remove] -= 1
                if counts[statuette_to_remove] == 0:
                    types_found -= 1
            
            left += 1

    print(min_cost)

if __name__ == "__main__":
    main()