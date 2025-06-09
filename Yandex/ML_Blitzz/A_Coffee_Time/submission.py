def score_function(params, r, d):
    """
    Calculates the goodness score for a coffee shop.
    S(r,d) = wr * r - wd * d + b
    """
    wr, wd, b = params
    return wr * r - wd * d + b

def main():
    optimal_wr, optimal_wd, optimal_b = 0.1301726308, 1.5460590234, 0.0000000210
    with open('restaurants.in', 'r') as f:
        n = int(f.readline().strip())
        for _ in range(n):
            r, d = map(float, f.readline().strip().split())
            score = score_function((optimal_wr, optimal_wd, optimal_b), r, d)
            print(score)

if __name__ == '__main__':
    main()

    