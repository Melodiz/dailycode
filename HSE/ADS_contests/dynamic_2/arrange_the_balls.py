def min_operations(balls):
    n = len(balls)
    lis = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if balls[i] > balls[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    
    return n - max(lis)

def main():
    n = int(input())
    balls = list(map(int, input().split()))
    print(min_operations(balls))

if __name__ == "__main__":
    main()