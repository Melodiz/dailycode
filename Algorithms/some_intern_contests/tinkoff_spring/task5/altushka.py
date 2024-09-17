def calculate_minutes(time_str, start_time):
    time_parts = list(map(int, time_str.split(":")))
    total_seconds = time_parts[0] * 3600 + time_parts[1] * 60 + time_parts[2]
    if total_seconds < start_time:
        total_seconds += 86400
    total_seconds -= start_time

    return total_seconds // 60

def main():
    requests = dict()
    server_data = [dict() for _ in range(100)]
    start_time = list(map(int, input().split(":")))
    start_time = start_time[0] * 3600 + start_time[1] * 60 + start_time[2]
    num_requests = int(input())
    for _ in range(num_requests):
        request = input().split()
        if request[0] not in requests:
            requests[request[0]] = []
        if request[0] not in server_data[ord(request[2])]:
            server_data[ord(request[2])][request[0]] = [0, 0]
        if request[3][0] == 'A':
            server_data[ord(request[2])][request[0]][1] = calculate_minutes(request[1], start_time)
            requests[request[0]].append(ord(request[2]))
        elif request[3][0] == 'D' or request[3][0] == 'F':
            server_data[ord(request[2])][request[0]][0] += 20

    results = []
    for user in requests:
        results.append([-len(requests[user]), 0, user])
        if results[-1][0] == 0:
            results[-1][0] = 10000
        for server in requests[user]:
            results[-1][1] += server_data[server][user][1]
            results[-1][1] += server_data[server][user][0]

    results.sort(key=lambda x: (x[0], x[1]))
    last_position = -1
    for i in range(len(results)):
        if not (last_position != -1 and results[i - 1][:2] == results[i][:2]):
            last_position = i
        if results[i][0] == 10000:
            results[i][0] = 0
        print(last_position + 1, results[i][2], -results[i][0], results[i][1])

if __name__ == "__main__":
    main()