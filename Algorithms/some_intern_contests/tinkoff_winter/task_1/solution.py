def main():
    s = input()
    r_index = s.index('R')
    m_index = s.index('M')

    if r_index < m_index:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()