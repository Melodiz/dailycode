def can_arrange_using_stack(arr):
    stack = []
    expected = 1  # Начинаем с самого срочного контейнера

    for urgency in arr:
        while stack and stack[-1] == expected:
            stack.pop()
            expected += 1
        if urgency == expected:
            expected += 1
        else:
            stack.append(urgency)

    while stack and stack[-1] == expected:
        stack.pop()
        expected += 1

    return 1 if not stack else 0

def main():
    n = int(input())
    arr = [list(map(float, input().split())) for _ in range(n)]
    for line in arr:
        print(can_arrange_using_stack(line[1:]))

if __name__ == "__main__":
    main()