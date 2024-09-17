def main():
    data = input().split(',')
    for item in data:
        item = item.strip().replace(',', '')
        if '-' in item:
            a,b = item.split('-')
            for i in range(int(a), int(b)+1):
                print(i, end=' ')
        else:
            print(item, end=' ')


if __name__ == '__main__':
    main()