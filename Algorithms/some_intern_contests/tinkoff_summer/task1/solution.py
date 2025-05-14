def main():
    s = input()
    for miss_idex in range(len(s)):
        new_s = s[:miss_idex] + s[miss_idex + 1:]
        if new_s == new_s[::-1]:
            print('YES')
            return
    print('NO')

if __name__ == "__main__":
    main()

# sine the max len(s) = 4, it's not a big deal to use this simple solution.