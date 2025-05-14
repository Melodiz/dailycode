from collections import Counter

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    unique = set(arr)
    cnt = Counter(arr)
    for i in range(n):
        if cnt[arr[i]] == 1:
            continue
        cnt[arr[i]] -= 1
        while arr[i] in unique and arr[i] > 0:
            arr[i] //= 2
        unique.add(arr[i])
    return len(set(arr))


if __name__ == "__main__":
    print(main())
