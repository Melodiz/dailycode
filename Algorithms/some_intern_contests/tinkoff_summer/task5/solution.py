def corners(x, y, a, b):
    if x == 0 and y == 0:
        return 0
    if x == 1 and y == 1:
        return min(a, 2 * b)
    if x == 2 and y == 0 or x == 0 and y == 2:
        return b
    if x == 0 or y == 0:
        return (max(x, y) // 2) * b
    if x == 1 or y == 1:
        return min(a, 2 * b) + ((max(x, y) - 1) // 2) * b
    return 0


def calc_cost(x, y, a, b):
    pairs = min(x, y) // 2
    if a < 2 * b:
        cost = pairs * a
        x -= 2 * pairs
        y -= 2 * pairs
    else:
        cost = pairs * 2 * b
        x -= 2 * pairs
        y -= 2 * pairs
    return cost + corners(x, y, a, b)

def optimal_solution(s, a, b):
    marked = [False] * len(s)
    left_parentheses = []

    for i, ch in enumerate(s):
        if ch == '(':
            left_parentheses.append(i)
        elif ch == ')' and left_parentheses:
            marked[i] = True
            marked[left_parentheses.pop()] = True

    cnt_open = cnt_close = 0
    for i, ch in enumerate(s):
        if not marked[i]:
            cnt_open += ch == '('
            cnt_close += ch == ')'
    return calc_cost(cnt_open, cnt_close, a, b)


def main():
    n, a, b = map(int, input().split())
    s = input()
    print(optimal_solution(s, a, b))


if __name__ == "__main__":
    main()
