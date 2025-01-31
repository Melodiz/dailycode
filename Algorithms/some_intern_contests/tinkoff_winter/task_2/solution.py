def generate_all_candidates(limit=10**18):
    candidates = []
    for i in range(60):
        for j in range(i+1, 60):
            for k in range(j+1, 60):
                val = (1 << i) + (1 << j) + (1 << k)
                if val <= limit:
                    candidates.append(val)
    candidates.sort()
    return candidates

def solve_query(x, candidates):
    import bisect
    idx = bisect.bisect_right(candidates, x) - 1
    return candidates[idx] if idx >= 0 else -1

def solve():
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    some_stuff = generate_all_candidates(max(nums)+10)
    
    for num in nums:
        print(solve_query(num, some_stuff))
    
if __name__ == "__main__":
    solve()