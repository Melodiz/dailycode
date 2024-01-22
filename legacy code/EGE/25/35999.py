a = 452_022

arr = []
M = []
X = []

for num in range(a, 10**14):
    if len(M) > 4:
        break
    for m in range(2, round(a**1/2)):
        if num % m == 0:
            x = int(m+num/m)
            if x % 7 == 3:
                M.append(x)
                X.append(num)
            break

for i in range(len(X)):
    print(X[i], M[i])


"""452025 150678

452029 23810

452034 226019

452048 226026

452062 226033

452021 2250
452025 150678
452029 23810
452034 226019
452048 226026"""