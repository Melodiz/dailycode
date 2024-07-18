# hanoe tower

def hanoi(n, source, target):
    if n == 1: # base case: only one disk to move
        print(source, target)
        return
    new_auxiliary = 6 - source - target
    hanoi(n-1, source, new_auxiliary)
    print(source, target)
    hanoi(n-1, new_auxiliary, target)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3)
