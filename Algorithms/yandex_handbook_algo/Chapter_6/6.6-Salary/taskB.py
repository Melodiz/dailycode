def max_wins(n, k, data):
    pivot = data[k-1]
    data = [pivot] + sorted([x for x in data if x != pivot])

    def iter(pivot, data):
        result = []
        for i in range(0, len(data)//2, 2):
            prev, cur = data[i], data[i+1]
            if prev > cur:
                result.append(prev)
                continue
            result.append(cur)
        if pivot not in result:
            return []
        return result

    def iter_odd(pivot, data):
        result = [data[0]]
        for i in range(1, len(data)//2 + 1, 2):
            prev, cur = data[i], data[i+1]
            if prev > cur:
                result.append(prev)
                continue
            result.append(cur)
        return result

    i = 0
    while len(data) > 1:
        if len(data) % 2 == 0:
            data = iter(pivot, data)
        else:
            data = iter_odd(pivot, data)
        i += 1
    return i

n, k = (map(int, input().split()))
data = list(map(int, input().split()))
print(max_wins(n, k, data))
