def main():
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, n):
        if arr[i] == -1:
            arr[i] = arr[i-1]+1 # заменить на arr[i] = arr[i-1]
        else:
            if arr[i] <= arr[i-1]: # here
                print('NO')
                return
    print('YES')
    print(arr[0], end = ' ')
    for i in range(1, n):
        print(arr[i]-arr[i-1], end=' ')
    return

if __name__ == '__main__':
    main()