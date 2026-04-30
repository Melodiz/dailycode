def main():
    n, m = map(int, input().split())
    values = []
    for epoch in range(n):
        vals = list(map(int, input().split()))
        vals = [(x, epoch) for x in vals]
        values.extend(vals)
    values.sort()
    best_val, best_left, best_right = values[-1][0] - values[0][0], 0, len(values)-1
    left, right = 0, 0
    current_map = dict([(x, 0) for x in range(n)])
    current_map[values[left][1]] += 1
    covered = 1
    while right < len(values):
        # if valid: 
        if covered == n:
            if values[right][0] - values[left][0] < best_val:
                best_val = values[right][0] - values[left][0]
                best_left, best_right = left, right
        # try to shrink from left
        if current_map[values[left][1]] > 1: 
            current_map[values[left][1]] -= 1
            left += 1
        else:
            right += 1
            if right < len(values):
                current_map[values[right][1]] += 1
                if current_map[values[right][1]] == 1: covered += 1
    ans = []
    collected_epochs = set()
    for v, e in values[best_left:best_right+1]:
        if e not in collected_epochs:
            ans.append(v)
            collected_epochs.add(e)
    print(*ans)
    

if __name__ == "__main__":
    main()