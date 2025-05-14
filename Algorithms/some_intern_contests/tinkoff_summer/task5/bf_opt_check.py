import sys
from collections import deque


def is_correct_seq(seq: str) -> bool:
    cnt = 0
    for par in seq:
        if par == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False

    return cnt == 0


def brute(init_seq: str, a: int, b: int) -> int:
    if is_correct_seq(init_seq):
        return 0

    n = len(init_seq)
    sequences = deque([(init_seq, 0)])
    seq_dict = {init_seq: 0}
    min_price = float('inf')

    while sequences:
        curr_seq, curr_price = sequences.popleft()

        # swaps
        new_price = curr_price + a
        for i in range(n - 1):
            for j in range(i + 1, n):
                new = list(curr_seq)
                new[i], new[j] = new[j], new[i]
                new_seq = ''.join(new)
                if is_correct_seq(new_seq):
                    if new_seq in seq_dict:
                        if new_price < seq_dict[new_seq]:
                            seq_dict[new_seq] = new_price
                            min_price = min(min_price, new_price)
                        else:
                            continue
                    else:
                        seq_dict[new_seq] = new_price
                        min_price = min(min_price, new_price)
                else:
                    if new_seq in seq_dict:
                        if new_price < seq_dict[new_seq]:
                            seq_dict[new_seq] = new_price
                            sequences.append((new_seq, new_price))
                        else:
                            continue
                    else:
                        seq_dict[new_seq] = new_price
                        sequences.append((new_seq, new_price))

        # negations
        new_price = curr_price + b
        for i in range(n):
            new = list(curr_seq)
            if new[i] == '(':
                new[i] = ')'
            else:
                new[i] = '('
            new_seq = ''.join(new)
            if is_correct_seq(new_seq):
                if new_seq in seq_dict:
                    if new_price < seq_dict[new_seq]:
                        seq_dict[new_seq] = new_price
                        min_price = min(min_price, new_price)
                    else:
                        continue
                else:
                    seq_dict[new_seq] = new_price
                    min_price = min(min_price, new_price)
            else:
                if new_seq in seq_dict:
                    if new_price < seq_dict[new_seq]:
                        seq_dict[new_seq] = new_price
                        sequences.append((new_seq, new_price))
                    else:
                        continue
                else:
                    seq_dict[new_seq] = new_price
                    sequences.append((new_seq, new_price))

    return min_price


def main():
    assert brute('())(((', 4, 3) == 7
    assert brute('()()()', 4, 3) == 0
    assert brute(')()(()()', 3, 2) == 3

    # Additional test cases
    assert brute('(())', 5, 2) == 0  
    assert brute('((((', 3, 4) == 8  
    assert brute('))((', 1, 5) == 1
    assert brute(')(', 10, 1) == 2
    print("All tests passed!")


if __name__ == '__main__':
    main()