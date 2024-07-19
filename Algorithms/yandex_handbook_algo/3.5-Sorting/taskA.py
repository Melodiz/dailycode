def selectionSort(data):
    for i in range(len(data)):
        cur_min = 10**10
        index = 0
        for j in range(i, len(data)):
            if data[j] < cur_min:
                cur_min = data[j]
                index = j
        data[i], data[index] = data[index], data[i]
    return data


n = int(input())
data = [int(x) for x in input().split()]

data = selectionSort(data)

print(' '.join(list(map(str, data))))
