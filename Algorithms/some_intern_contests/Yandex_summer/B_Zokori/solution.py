def main():
    n = int(input())

    total_pairs = n * (n - 1) // 2
    
    marker_map = {chr(ord('C') + i): i for i in range(10)}
    
    num_markers = 10
    max_masks = 1 << num_markers
    
    counts = [0] * max_masks
    
    for _ in range(n):
        s = input().strip()
        mask = 0
        for char in set(s):
            if char in marker_map:
                mask |= (1 << marker_map[char])
        counts[mask] += 1
        
    sos_dp = list(counts)
    for i in range(num_markers):
        for mask in range(max_masks):
            if (mask >> i) & 1:
                sos_dp[mask] += sos_dp[mask ^ (1 << i)]

    disjoint_pairs_sum = 0
    all_markers_mask = max_masks - 1
    
    for mask in range(max_masks):
        if counts[mask] > 0:
            complement_mask = all_markers_mask ^ mask
            num_disjoint_fragments = sos_dp[complement_mask]
            
            disjoint_pairs_sum += counts[mask] * num_disjoint_fragments
            
    num_disjoint_pairs = disjoint_pairs_sum // 2
    
    result = total_pairs - num_disjoint_pairs
    print(result)

if __name__ == "__main__":
    main()