# def check_brute(arr):
#     n = len(arr)
#     count = 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):
#                 if arr[j] - arr[i] == arr[k] - arr[j]:
#                     return True
#     return False

def smart_check(arr):
    c1 = set()
    c2 = set()
    for d in range(-4, 5):
        for i in range(len(arr)):
            if arr[i] in c2: return True
            if arr[i] in c1: c2.add(arr[i]+d)
            c1.add(arr[i]+d)
        c1.clear(); c2.clear()
    return False

def brute(arr):
    counter = 0
    for i in range(len(arr)+1):
        for j in range(i+3, len(arr)+1):
            counter += smart_check(arr[i:j])
            # if smart_check(arr[i:j]) == True: print(arr[i:j])

    return counter

if __name__ == "__main__":
    arr = [1, 2, 3, 3, 2, 1]
    arr2 = [5, 1, 3, 5, 2, 5]
    arr3 = [1, 4, 7, 5, 3, 8, 9, 5, 7, 1]
    print(brute(arr)) # 3
    print(brute(arr2)) # 6 
    print(brute(arr3)) # 26