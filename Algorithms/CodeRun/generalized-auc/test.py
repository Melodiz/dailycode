# def read_data():
#     n = int(input())
#     if n <= 20:
#         row_data = [list(map(float, input().split())) for _ in range(n)]
#     elif n == 1000:
#         row_data = [list(map(int, input().split())) for _ in range(n)]
#     else:
#         row_data = [list(map(float, input().split())) for _ in range(n)]
#     return n, row_data

def read_data_file(file_path = 'input.txt'):
    with open(file_path, 'r') as f:
        n = int(f.readline().strip())
        if n <= 20:
            row_data = [list(map(float, line.strip().split())) for line in f]
        elif n == 1000:
            row_data = [list(map(int, line.strip().split())) for line in f]
        else:
            row_data = [list(map(float, line.strip().split())) for line in f]
    return n, row_data

def generalized_auc(n, data):
    numerator = 0
    denominator = 0
    for i in range(n):
        for j in range(n):
            if data[i][0] > data[j][0]:
                denominator += 1
                numerator += data[i][1] > data[j][1]
                numerator += 0.5 * (data[i][1] == data[j][1])
    return numerator / denominator

def main():
    n, row_data = read_data_file()
    result = generalized_auc(n, row_data)
    print(result)

def base_test():
    data = [[0, 0], [1, 1]]
    assert abs(generalized_auc(2, data) - 1) < 1e-6
    data = [[0, 1], [1, 0]]
    assert abs(generalized_auc(2, data) - 0) < 1e-6
    data = [[0.5, 0], [0.5, 1], [2, 0.5]]
    assert abs(generalized_auc(3, data) - 0.5) < 1e-6
    data = [[0, 0], [0, 1], [1, 2], [0, 3], [1, 4], [1, 5], [1, 6]]
    assert abs(generalized_auc(7, data) - 0.916667) < 1e-6
    data = [[0, 4], [3, 0], [1, 2], [2, 4], [1, 0], [2, 1], [4, 1], [2, 1], [4, 4], [0, 0]]
    assert abs(generalized_auc(10, data) - 0.538462) < 1e-6
    data = [[3, 4], [3, 4], [2, 1], [3, 2], [4, 1], [0, 2], [2, 0], [1, 2], [4, 4], [3, 3]]
    assert abs(generalized_auc(10, data) - 0.648649) < 1e-6
    print("All tests passed")

if __name__ == "__main__":
    base_test()
    main()