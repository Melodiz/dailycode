def next_train_time(a, b, arrival_time):
    if arrival_time <= a:
        return a
    last_train_time = a + ((arrival_time - a) // b) * b
    return last_train_time + b if last_train_time != arrival_time else arrival_time

def main():
    schedules = []
    for _ in range(int(input())):
        a, b = map(int, input().split())
        schedules.append((a, b))
    for _ in range(int(input())):
        t, d = map(int, input().split())
        print(next_train_time(*schedules[t-1], d))

if __name__ == "__main__":
    main()