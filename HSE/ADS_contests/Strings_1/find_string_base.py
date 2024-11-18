def prefix_function(text):
    n = len(text)
    p = [0] * n
    for i in range(1, n):
        j = p[i - 1]
        while j > 0 and text[i] != text[j]:
            j = p[j - 1]
        if text[i] == text[j]:
            j += 1
        p[i] = j
    return p

def find_minimal_length(text):
    p = prefix_function(text)
    n = len(text)
    # The minimal length of the original string S
    minimal_length = n - p[-1]
    return minimal_length

def main():
    text = input().strip()
    print(find_minimal_length(text))

if __name__ == "__main__":
    main()