import math
from itertools import combinations, product

def cost_to_divisible(a, d):
    """
    Returns how many increments are needed to make 'a' divisible by 'd'.
    That is:  cost = (d - (a mod d)) mod d.
    """
    r = a % d
    if r == 0:
        return 0
    return d - r

def brute_solution(n, x, y, z, arr):
    """
    Brute-force approach:
      1) Precompute cost_to_cover_mask(a, mask) for each a in arr and mask in {1..7}.
      2) Try every subset of arr of size 1..3.
      3) For each subset, try all ways to distribute the three conditions (x, y, z)
         (represented by bitmask 1..4..2 = 1,2,4) across the chosen elements
         so that the union of condition-subsets is {1,2,4} (bitmask=7).
      4) Minimize the total cost.
    """
    # Map each bitmask 1..7 to the corresponding LCM of the needed divisors among x, y, z
    #    bit 0 (value 1) => x
    #    bit 1 (value 2) => y
    #    bit 2 (value 4) => z
    # mask = 1 => lcm(x)
    # mask = 2 => lcm(y)
    # mask = 3 => lcm(x,y)
    # mask = 4 => lcm(z)
    # mask = 5 => lcm(x,z)
    # mask = 6 => lcm(y,z)
    # mask = 7 => lcm(x,y,z)
    divisors = [(1, x), (2, y), (4, z)]  # (bit, value)
    
    # Precompute the LCM for each mask from 1..7
    lcm_for_mask = [0]*8
    for mask in range(1, 8):
        # collect divisors belonging to this mask
        ds = []
        for bit, val in divisors:
            if mask & bit:
                ds.append(val)
        # compute LCM of those
        l = 1
        for d in ds:
            l = (l*d)//math.gcd(l, d)
        lcm_for_mask[mask] = l
    
    # Precompute cost[a_index][mask] = cost to make arr[a_index] cover the subset of conditions in mask
    # That is cost to make arr[a_index] divisible by lcm_for_mask[mask].
    cost_array = []
    for a in arr:
        row = [0]*8
        for mask in range(1, 8):
            row[mask] = cost_to_divisible(a, lcm_for_mask[mask])
        cost_array.append(row)
    
    # If it's possible that one element covers everything, we look up cost of bitmask=7
    # Now we brute force over subsets of the array of size 1..3
    best = float('inf')
    # We only need up to 3 elements because there are 3 conditions in total
    for subset_size in (1, 2, 3):
        for indices in combinations(range(n), subset_size):
            # Try to assign each of the 3 conditions (bits 1,2,4 => 7 total) among these subset_size elements
            # We'll do a small "mask assignment": each chosen element gets a mask in [0..7].
            # Then the union of those masks must be 7 (meaning x, y, z are all covered).
            
            # Because subset_size <= 3, we can simply try all possible masks for each element:
            # That's 7^subset_size ways in the worst case (excluding mask=0 because that covers no condition).
            # But we can allow mask=0 if we want, as it won't help but might skip a condition. We'll skip 0 so we
            # don't have an element that covers nothing (it wouldn't reduce cost).
            
            # We'll gather the minimal sum of costs among the ways that achieve union=7.
            
            local_best = float('inf')
            all_masks = range(1, 8)  # from 1..7
            # For the chosen subset_size elements, do a cartesian product of possible masks
            for chosen_masks in product(all_masks, repeat=subset_size):
                union_mask = 0
                for m in chosen_masks:
                    union_mask |= m
                if union_mask == 7:
                    # covers x,y,z
                    total_cost = 0
                    for idx_el, ms in zip(indices, chosen_masks):
                        total_cost += cost_array[idx_el][ms]
                    if total_cost < local_best:
                        local_best = total_cost
            
            best = min(best, local_best)
    
    return best

def solve():
    import sys
    data = sys.stdin.read().strip().split()
    n, x, y, z = map(int, data[:4])
    arr = list(map(int, data[4:]))

    # For large n, this brute force is NOT practical.
    # It is only for small n testing. Use with caution!
    print(brute_solution(n, x, y, z, arr))

# -----------------------
# A quick demonstration of usage:
if __name__ == "__main__":
    solve()