def piggy_bank_min(F, N, coins):
    # Инициализация массива для динамического программирования
    min_sum = [float('inf')] * (F + 1)
    min_sum[0] = 0
    
    # Заполнение массива dp
    for w in range(1, F + 1):
        for value, coin_weight in coins:
            if coin_weight <= w:
                min_sum[w] = min(min_sum[w], min_sum[w - coin_weight] + value)
    
    return min_sum[F] if min_sum[F] != float('inf') else -1

def piggy_bank_max(F, N, coins):
    # Инициализация массива для динамического программирования
    max_sum = [float('-inf')] * (F + 1)
    max_sum[0] = 0
    
    # Заполнение массива dp
    for w in range(1, F + 1):
        for value, coin_weight in coins:
            if coin_weight <= w:
                max_sum[w] = max(max_sum[w], max_sum[w - coin_weight] + value)
    
    return max_sum[F] if max_sum[F] != float('-inf') else -1

def main():
    E, F = map(int, input().split())
    N = int(input())
    coins = [tuple(map(int, input().split())) for _ in range(N)]

    weight = F - E  # Вес монет в копилке
    lower = piggy_bank_min(weight, N, coins)
    if lower == -1:
        print('This is impossible.')
    else:
        upper = piggy_bank_max(weight, N, coins)
        print(lower, upper)

if __name__ == "__main__":
    main()