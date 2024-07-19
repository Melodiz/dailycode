def Lomuto_partition(data, pivot):
    i = 0
    for j in range(1, len(data)):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
    data[0], data[i] = data[i], data[0]
    return data


n = int(input())
data = [int(x) for x in input().split()]
data = Lomuto_partition(data, data[0])
print(' '.join(map(str, data)))