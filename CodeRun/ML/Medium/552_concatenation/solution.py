def check(a, b):
    # check if a + b is tandem: means length of a + b is even and left and right parts are equal
    mid = (len(a)+len(b)) // 2
    a += b
    return a[:mid] == a[mid:]


def main():
    n = int(input())
    repeats_map = {}
    strings = []
    for t in range(n):
        s = input()
        if s in repeats_map:
            repeats_map[s].append(t)
        else:
            repeats_map[s] = [t]
            strings.append(s)

    for i in range(n):
        for j in range(i + 1, n):
            if (len(strings[i]) + len(strings[j])) % 2 == 0:
                if check(strings[i], strings[j]):
                    for k in repeats_map[strings[i]]:
                        for l in repeats_map[strings[j]]:
                            print(k+1, l+1)
                            print(l+1, k+1)


if __name__ == "__main__":
    main()
