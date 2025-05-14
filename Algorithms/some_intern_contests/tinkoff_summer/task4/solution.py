def solve(arr):
    data = [[-1 for _ in range(11)] for _ in range(len(arr))]
    closest = [-1]*11
    max_seen = -1
    ans = 0
    for i in range(len(arr)):
        for k in range(1, 11):
            data[i][k] = closest[k]
        closest[arr[i]] = i
        closest_left = -1
        for d in range(-4, 5):
            # find first left
            if arr[i]+d < 0 or arr[i]+d > 10:
                continue
            b_index = data[i][arr[i]+d]
            if b_index == -1 or arr[b_index]+d < 0 or arr[b_index]+d > 10:
                continue
            a_index = data[b_index][arr[b_index]+d]
            if a_index == -1:
                continue
            closest_left = max(closest_left, a_index)
        ans += max(closest_left + 1, max_seen + 1)
        max_seen = max(max_seen, closest_left)
    return ans

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))


if __name__ == "__main__":
    main()
