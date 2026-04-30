def main():
    n, q = map(int, input().split())
    rewards = list(map(int, input().split()))
    frequencies = [0] * (n + 1)
    for _ in range(q):
        l, r = map(int, input().split())
        frequencies[l - 1] += 1
        frequencies[r] -= 1
    # prefix sum
    for i in range(1, n):
        frequencies[i] += frequencies[i - 1]
    frequencies = frequencies[:n]
    rewards.sort()
    frequencies.sort()
    total_reward = 0
    for i in range(n):
        total_reward += rewards[i] * frequencies[i]
    print(total_reward)

if __name__ == "__main__":
    main()
