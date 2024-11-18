def z_to_prefix(z):
    p = [0] * len(z)
    for i in range(1, len(z)):
        for j in range(z[i] - 1, -1, -1):
            if p[i + j] > 0:
                break
            else:
                p[i + j] = j + 1
    return p

def main():
    n = int(input().strip())
    z = list(map(int, input().strip().split()))
    prefix = z_to_prefix(z)
    print(*prefix)

if __name__ == "__main__":
    main()