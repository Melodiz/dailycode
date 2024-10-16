def main():
    arr = []
    with open('input.txt', 'r') as file:
        for line in file:
            line_value = line.strip().split()
            arr.append([int(line_value[0]), line_value[1]])
    
    arr.sort(key=lambda x: (x[0]))
    for item in arr:
        print(*item)
    return 0

if __name__ == "__main__":
    main()
    
