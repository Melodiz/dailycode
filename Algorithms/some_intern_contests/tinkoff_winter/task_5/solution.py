def solve_5():
    rod_length, max_weight = map(int, input().split())
    weights = list(map(int, input().split()))
    weights.insert(0, 0)

    cut_points = []
    current_weight = 0

    for i in range(1, rod_length + 1):
        if current_weight + weights[i] <= max_weight:
            current_weight += weights[i]
        else:
            cut_points.append(i - 1)
            current_weight = weights[i]

    total_subrods = rod_length * (rod_length + 1) // 2
    additional_subrods = sum(cut * (rod_length - cut) for cut in cut_points)

    print(total_subrods + additional_subrods)

def main():
    solve_5()

if __name__ == "__main__":
    main()