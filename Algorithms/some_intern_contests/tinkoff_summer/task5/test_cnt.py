from tqdm import tqdm

def corners(x, y, a, b):
    if x == 0 and y == 0: return 0
    if x == 1 and y == 1: return min(a, 2*b)
    if x == 2 and y == 0 or x == 0 and y == 2: return b
    if x == 0 and y > 2: return y//2 * b
    if y == 0 and x > 2: return x//2 * b
    if x == 1 and y > 2: return min(a, 2*b)+ (y-1)//2 * b
    if y == 1 and x > 2: return min(a, 2*b)+ (x-1)//2 * b


def rest(cnt_open, cnt_close, a, b):
    cost = 0
    while min(cnt_open, cnt_close) >= 2:
        if a < 2*b: # cheaper than 4 changes
            cost += a
            cnt_open -= 2
            cnt_close -= 2
        else:
            cost += b
            if cnt_open > cnt_close: 
                cnt_open -=2
            else:
                cnt_close -=2
    # if cnt_open == 0 and cnt_close == 0: return cost
    # if cnt_open == 0 and cnt_close > 0: return cost + b * cnt_close//2
    # if cnt_open > 0 and cnt_close == 0: return cost + b * cnt_open//2
    # if cnt_close == 1: 
    #     if a<2*b:return cost + min(a, 2*b) + ((cnt_open-1)//2)*b
    #     else: return cost 
    # if cnt_open == 1: return cost + min(a, 2*b) + ((cnt_close-1)//2)*b
    # return -1
    return cost + corners(cnt_open, cnt_close, a, b)
        

def optimal_solution(s, a, b):
    # First pass: match valid parentheses pairs
    marked = [False] * len(s)
    left_parentheses = []
    
    for i, ch in enumerate(s):
        if ch == '(':
            left_parentheses.append(i)
        elif ch == ')' and left_parentheses:
            marked[i] = True
            marked[left_parentheses.pop()] = True
    
    # Count unmatched parentheses in a single pass
    cnt_open = cnt_close = 0
    for i, ch in enumerate(s):
        if not marked[i]:
            cnt_open += ch == '('
            cnt_close += ch == ')'
    return rest(cnt_open, cnt_close, a, b)



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

def test_case():
    import random
    for _ in tqdm(range(1000000)):
        n = random.randint(1, 10)
        s = ''.join(random.choice('()') for _ in range(n))
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        brute_ans = brute(s, a, b) 
        if brute_ans > 100000: continue
        optimized_ans = optimal_solution(s, a, b)
        assert brute_ans == optimized_ans, f"Test failed for n={n}, s={s}, a={a}, b={b}, brute_ans={brute_ans}, optimized_ans={optimized_ans}  \n"
    print("All tests passed!")


if __name__ == "__main__":
    test_case()

