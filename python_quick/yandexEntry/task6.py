def searchInsert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

# file = open("input.txt", "r")
# M = int(file.readline())
# K = int(file.readline())
# metric_values = list(map(int, file.readline().split()))
M = int(input())
K = int(input())
metric_values = list(map(int, input().split()))

data = [metric_values[j] for j in range(K)]
data.sort()
ld = len(data)-1

flag = True
for i in range(K, len(metric_values)):
    if data[-int(len(data)*0.9)] < metric_values[i]:
        flag = False
        print(i+1)
        break
    ind = searchInsert(data, metric_values[i])
    data = data[:ind] + [metric_values[i]] + data[ind:]
    ld+=1

if flag:
    print(-1)


