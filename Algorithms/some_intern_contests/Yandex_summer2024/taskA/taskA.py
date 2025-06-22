def main():
    N, K, t = map(int, input().split())

    heights = []
    target_value = 0

    for i in range(N):
        height = int(input())
        if i + 1 == t:
            target_value = height
        else:
            heights.append(height)
    if K == 1:
        print(0)
        return
    N -= 1
    heights.sort()
    minimum_difference = float('inf')
    K -= 1
    for i in range(N - K + 1):
        current_difference = max(heights[i + K - 1] - heights[i], abs(target_value -
                  heights[i]), abs(heights[i + K - 1] - target_value))
        minimum_difference = min(minimum_difference, current_difference)

    print(minimum_difference)


if __name__ == "__main__":
    main()
