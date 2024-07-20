def getSings(data):
    result = []
    while len(data):
        new = []
        r = data.pop(0)[1]
        result.append(r)
        for i in range(len(data)):
            if data[i][0] > r:
                new.append(data[i])
        data = new
    return result



n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

data.sort(key=lambda x: x[1])

result = getSings(data)
print(len(result))
print(' '.join(map(str, result)))
