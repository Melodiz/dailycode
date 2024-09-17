from solution import solve


def read_data(file_path='task3/test_cases.txt'):
    cases = []
    expected_outputs = []
    with open(file_path, 'r') as file:
        arr = file.readlines()
        for i in range(0, len(arr), 4):
            cases.append((arr[i].strip(),
                          arr[i+1].strip(), int(arr[i+2].strip())))
            expected_outputs.append(arr[i+3].strip())
    return cases, expected_outputs


def run_tests():
    from tqdm import tqdm
    import time
    cases, expected_outputs = read_data()
    for i, (data_string, alphabet_set, max_length) in enumerate(cases):
        output = solve(data_string, alphabet_set, max_length)
        assert expected_outputs[i] == output, \
            f'Test case {i+1} failed: expected {expected_outputs[i]}, got {output}'
    print('Tinkoff test cases passed.')

    cases, expected_outputs = read_data('task3/random_test_cases.txt')
    starttime = time.time()
    for i in tqdm(range(len(cases)), desc='Random test cases'):
        output = solve(cases[i][0], cases[i][1], cases[i][2])
        assert expected_outputs[i] == str(output), \
            f'Random test case {i+1} failed: expected {expected_outputs[i]}, got {output}'
    endtime = time.time()
    print(
        f'Random test cases passed in {round(endtime - starttime, 4)} seconds.')


if __name__ == "__main__":
    run_tests()
