import random


def check(data):
    for i in range(3):
        for j in range(3):
            if i == j and abs(data[i][j]) != 1:
                return False
            else:
                if data[i][j] != 0:
                    return False
    return True


def row_change(data, n1, n2):
    data[n1], data[n2] = data[n2], data[n1]
    return data


def col_change(data, n1, n2):
    # n1 -= 1
    # n2 -= 1
    ans = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            if j == n1:
                ans[i][j] = data[i][n2]
            elif j == n2:
                ans[i][j] = data[i][n1]
            else:
                ans[i][j] = data[i][j]
    return ans


def change(data, n1, n2):
    n1 -= 1
    n2 -= 1
    # data = row_change(data, n1, n2)
    data = col_change(data, n1, n2)
    print(f'change {n1+1} with {n2+1}')
    for j in range(3):
        print(data[j])
    print()
    if check(data):
        print('Succsess')
        return
    return data


def row_sub(data, n1, n2, coef):
    for i in range(3):
        data[n2][i] += data[n1][i]*coef
    return data


def col_sub(data, n1, n2, coef):
    for i in range(3):
        data[i][n2] += data[i][n1]*coef
    return data


def sub(data, n1, n2, coef):
    n1 -= 1
    n2 -= 1
    # data = row_sub(data, n1, n2, coef)
    data = col_sub(data, n1, n2, coef)
    print(f'sub {coef}*{n1+1} from {n2+1}')
    for j in range(3):
        print(data[j])
    if check(data):
        print("Succsess")
        return
    return data


def mult(data, n1, coef):
    n1 -= 1
    # for i in range(3):
    #     data[n1][i] *= coef
    for i in range(3):
        data[i][n1] *= coef
    print(f'Mult {n1+1} on {coef}')
    for j in range(3):
        print(data[j])
    if check(data):
        print('Succsess')
        return
    return data


def to_int(data):
    for i in range(3):
        for j in range(3):
            data[i][j] = int(data[i][j])
    for i in range(3):
        print(data[i])
    return data


# data = [
#     [1, 1, 1],
#     [1, 1, -1],
#     [1, -1, 1],
# ]
# data = change(data, 2, 3)
# data = sub(data, 2, 3, 1)
# data = sub(data, 1, 3, -1)
# data = sub(data, 1, 2, -1)
# data = sub(data, 1, 3, -1)
# data = mult(data, 3, -1/2)
# data = to_int(data)
# data = change(data, 2, 3)
# data = sub(data, 2, 3, 1)

print('______________')
data = [
    [1, 0, 0], 
    [0, 1, 0],
    [0, 0, 1]
]
data = change(data, 2, 3)
data = sub(data, 2, 3, 1)
data = sub(data, 1, 3, -1)
data = sub(data, 1, 2, -1)
data = sub(data, 1, 3, -1)
data = mult(data, 3, -1/2)
data = to_int(data)
data = change(data, 2, 3)
data = sub(data, 2, 3, 1)

# data = sub(data, 3, 1, -1)
# data = sub(data, 3, 2, 1)
# data = mult(data, 1, 1/2)
# data = to_int(data)

# for t in range(1_000_000):
#     n1 = random.choice([1, 2, 3])
#     n2 = random.choice([1, 2, 3])

#     data = change(data, n1, n2)
