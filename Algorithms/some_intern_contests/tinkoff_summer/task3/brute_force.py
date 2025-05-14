from collections import Counter

def process(arr, n):
    cnt = Counter(arr)
    while max(cnt.values()) > 1:
        max_val, max_index = -1, -1
        for i in range(len(arr)):
            if cnt[arr[i]] > 1 and arr[i] > max_val:
                max_val, max_index = arr[i], i
        tmp = arr[max_index] //2
        cnt[arr[max_index]] -= 1
        if arr[tmp] in cnt:
            cnt[arr[tmp]] += 1
        else:
            cnt[arr[tmp]] = 1
    return len(cnt.keys())

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = Counter(arr)


