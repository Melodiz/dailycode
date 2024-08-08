def read_data():
    n = int(input())
    if n <= 20:
        row_data = [list(map(float, input().split())) for _ in range(n)]
    elif n == 1000:
        row_data = [list(map(int, input().split())) for _ in range(n)]
    else:
        row_data = [list(map(float, input().split())) for _ in range(n)]
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
    n, row_data = read_data()
    result = generalized_auc(n, row_data)
    print(result)

if __name__ == "__main__":
    main()