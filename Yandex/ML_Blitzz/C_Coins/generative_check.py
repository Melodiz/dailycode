import random
from main import solve_coin_ordering
from tqdm import tqdm

def generate_test_case(num_coins = 100, min_k = 1, max_k = 50):
    true_p_values = [random.uniform(0, 1) for _ in range(num_coins)]
    solver_input_data = []

    for i in range(num_coins):
        p_true = true_p_values[i]
        k_i = random.randint(min_k, max_k)
        m_i = 0
        if k_i > 0:
            m_i = sum(1 for _ in range(k_i) if random.random() < p_true)
        solver_input_data.append([k_i, m_i])
    index_to_p_map = {i: p for i, p in enumerate(true_p_values)}
    return solver_input_data, index_to_p_map

def test_ordering_accuracy(ordering, index_to_p_map):
    total_pairs = 0
    true_pairs = 0
    for i in range(len(ordering)):
        for j in range(i + 1, len(ordering)):
            total_pairs += 1
            if index_to_p_map[ordering[i]] <= index_to_p_map[ordering[j]]:
                true_pairs += 1
    try:
        return true_pairs / total_pairs
    except ZeroDivisionError:
        print(ordering, index_to_p_map)
        raise

def main():
    total_accuracy = 0
    cases = 10
    for i in tqdm(range(cases)):
        test_data, index_to_p_map = generate_test_case(10000)
        ordering = solve_coin_ordering(test_data)
        accuracy = test_ordering_accuracy(ordering, index_to_p_map)
        total_accuracy += accuracy
    print(total_accuracy / cases)

main()

