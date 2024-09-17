def solver(data_string, allowed, maxLength):
    dict1 = {}
    set1 = set(allowed)
    ans = (None, None)
    for key in list(set1):
        dict1[key] = dict1.get(key, 0) + 1
    l = 0
    def check(dict1, keys):
        empty = True
        for item in dict1:
            # if (item in set1 and dict1[item] > 0) or (item not in keys and dict1[item]!=0):
            #     empty = False
            #     break
            if (item in set1) and dict1[item] > 0:
                empty = False
                break
            elif (item not in set1 and dict1[item]!=0):
                empty = False
                break
        return empty
    for r in range(len(data_string)):
        bukva = data_string[r]
        if bukva not in set1:
            while l <= r:
                if check(dict1, allowed):
                    ans = (l, r-1)
                if data_string[l] in set1:
                    dict1[data_string[l]]+=1
                l+=1
            # for j in range(l, r):
            #     if nabor[j] in set1:
            #         dict1[nabor[j]]+=1
            # l = r
            # continue
        else:
            dict1[bukva]-=1
        if check(dict1, allowed):
            ans = (l, r)
        # while l < r and check(dict1, keys):
        #     if nabor[l] in set1:
        #         dict1[nabor[l]] = dict1.get(nabor[l], 0) + 1
        #     l+=1
        #     ans = (l, l+maxLength)
        if (r-l+1) == maxLength:
            if data_string[l] in dict1:
                dict1[data_string[l]]+=1
                l+=1
    while l <= r and check(dict1, allowed):
        ans = (l, l+maxLength)
        if data_string[l] in dict1:
            dict1[data_string[l]]+=1
        l+=1
    #print(ans)
    left, right = ans
    if left is None:
        return -1
    else:
        for i in range(right+1, min(r+maxLength, len(bukva))):
            if data_string[i] in set1:
                right+=1
        return data_string[left:right+1]


def read_data(file_path='task3/test_cases.txt'):
    cases = []
    expected_outputs = []
    with open(file_path, 'r') as file:
        arr = file.readlines()
        for i in range(0, len(arr), 4):
            cases.append((arr[i].strip(), set(
                arr[i+1].strip()), int(arr[i+2].strip())))
            expected_outputs.append(arr[i+3].strip())
    return cases, expected_outputs

def run_tests():
    cases, expected_outputs = read_data()
    for i, (data_string, alphabet_set, max_length) in enumerate(cases):
        output = solver(data_string, alphabet_set, max_length)
        assert expected_outputs[i] == output, \
            f'Test case {i+1} failed: expected {expected_outputs[i]}, got {output}'
    print('All test cases passed.')


def generate_random_test_cases(num_test_cases=100, n=2*10**5):
    import random
    from tqdm import tqdm
    test_cases = []
    expected_outputs = []
    full_alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for _ in tqdm(range(num_test_cases), desc='Generating test cases'):
        allowed_alphabet = list(random.sample(full_alphabet, random.randint(1, 26)))
        test_case_alphabet = set(allowed_alphabet + list(random.sample(full_alphabet, random.randint(1, 26))))
        max_length = random.randint(1, n)
        data_string = ''.join(random.choice(full_alphabet) for _ in range(n))
        test_cases.append((data_string, test_case_alphabet, max_length))
        expected_outputs.append(solver(data_string, test_case_alphabet, max_length))
    with open('task3/large_tests.txt', 'w') as file:
        for i in range(num_test_cases):
            file.write(f'{test_cases[i][0]}\n')
            file.write(''.join(sorted(test_cases[i][1])) + '\n')
            file.write(str(test_cases[i][2]) + '\n')
            file.write(f'{expected_outputs[i]}\n')
    print('Generated', num_test_cases, 'random test cases.')

if __name__ == "__main__":
    run_tests()
    generate_random_test_cases()
