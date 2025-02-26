def naive(string, start, current):
    ans = 0
    while current < len(string) and string[current] == string[start]:
        current += 1
        ans += 1
        start += 1
    return ans


def z_function(text):
    z = [0]*len(text)
    left, right = 0, 0
    for i in range(1, len(text)):
        if i > right:
            z[i] = naive(text, 0, i)
            left, right = i, z[i]-1
        else:
            k = i-left
            if i + z[k] <= right:
                z[i] = z[k]
            else:
                z[i] = right - i + naive(text, right-i, right)
                left, right = i, i + z[i] - 1
    return z


def KMP(text, pattern):
    concat = pattern + '$' + text
    l = len(pattern)
    z_array = z_function(concat)
    entrances = []
    for i in range(len(z_array)):
        if z_array[i] == l:
            entrances.append(i)
    return entrances


if __name__ == "__main__":
    text = "GEEKS FOR GEEKS"
    pattern = "GEEK"
    print(KMP(text, pattern))
