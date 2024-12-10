def last_fibonacci_number(n):
    if n <= 1:
        return 1
    
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 10
    
    return b

def main():
    n = int(input())
    print(last_fibonacci_number(n))

if __name__ == "__main__":
    main()