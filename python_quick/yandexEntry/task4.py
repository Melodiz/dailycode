import math
deadline = int(input())
tasks_per_project = sorted(list(map(int, input().split())))
# print(12//7)


def binary_search(deadline, tasks_per_project):
    low = 1
    high = max(tasks_per_project)+1

    while low < high:
        mid = (low + high) // 2
        # print(mid, check_can_or_not(deadline, tasks_per_project, mid))
        if check_can_or_not(deadline, tasks_per_project, mid):
            high = mid
        else:
            low = mid+1
    if check_can_or_not(deadline, tasks_per_project, low) and not check_can_or_not(deadline, tasks_per_project, low-1):
        return low
    else:
        for i in range(1, low):
            if not check_can_or_not(deadline, tasks_per_project, low-i):
                return low-i+1
    return 1
    


def check_can_or_not(deadline, tasks_per_project, limit):
    days = 0
    for task in tasks_per_project:
        # print(task, days)
        days += math.ceil(task/limit)
    if days <= deadline:
        return True
    return False


result = binary_search(deadline, tasks_per_project)
# print(check_can_or_not(deadline, tasks_per_project, 11))
print(result)
