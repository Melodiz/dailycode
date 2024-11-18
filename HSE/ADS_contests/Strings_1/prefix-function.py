def prefix_function(text):
    n = len(text)
    p = [0] * n
    for i in range(1, n):
        if text[p[i - 1]] == text[i]:
            p[i] = p[i - 1] + 1
        else:
            j = p[i - 1]
            while j > 0 and text[i] != text[j]:
                j = p[j - 1]
            if text[i] == text[j]:
                j += 1
            p[i] = j
    return p


def main():
    text = input()
    print(*prefix_function(text))

if __name__ == "__main__":
    main()