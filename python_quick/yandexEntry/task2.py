from functools import lru_cache

@lru_cache(None)
def searchInsert(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return mid
        
    return  l

# Пример использования функции
n = int(input())
k = int(input())
numbers = list(map(int, input().split()))
# result_index = find_index_greater_than_90_percent(numbers, k, n)
# print(result_index) 
data = sorted([numbers[j] for j in range(k)])

flag = True

for i in range(k, len(numbers)):
    ins = searchInsert(data, numbers[i])
    if ins >= (len(data)*0.9):
        print(i+1)
        flag = False
        break
    data = data[:ins] + [numbers[i]] + data[ins:]

if flag:
    print(-1)