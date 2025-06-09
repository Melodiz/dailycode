from itertools import permutations


def calculate_relevance(data):
    # data[i] = (class, rank)
    total_relevance = 2**(-data[0][1])
    for i in range(1, len(data)):
        if data[i][0] == data[i-1][0]:
            return -float('inf')
        total_relevance += 2**(-data[i][1])
    return total_relevance

def find_best_ordering(classes):
    data = [(c, i) for i, c in enumerate(classes)]
    best_ordering = data
    best_relevance = calculate_relevance(data)
    for combination in permutations(data):
        if calculate_relevance(combination[:7]) != -float('inf'):
            print([c[0] for c in combination[:7]], calculate_relevance(combination[:7]))
        comb_relevance = calculate_relevance(combination[:7])
        if comb_relevance > best_relevance:
            best_relevance = comb_relevance
            best_ordering = combination
    return best_ordering

def main():
    clases = [1, 1, 0, 0, 1, 0, 1, 1, 1]
    print(find_best_ordering(clases))

if __name__ == "__main__":
    main()