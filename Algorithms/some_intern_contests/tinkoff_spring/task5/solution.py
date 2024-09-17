def convert_time_to_seconds(time_str, start_time=None):
    hours, minutes, seconds = map(int, time_str.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    if start_time is None:
        return total_seconds
    if total_seconds > start_time:
        return (total_seconds - start_time) // 60
    return (total_seconds - start_time + 86400) // 60


def main():
    initial_time = convert_time_to_seconds(input())
    num_entries = int(input())
    team_data = {}
    successful_teams = {}
    data = []
    for _ in range(num_entries):
        team_name, timestamp, server_id, response_code = input().split()
        timestamp = convert_time_to_seconds(timestamp, initial_time)
        data.append([timestamp, team_name, server_id, response_code])
    data.sort()

    for elapsed_time, team_name, server_id, response_code in data:
        if team_name not in team_data:
            team_data[team_name] = []
        if team_name not in successful_teams:
            successful_teams[team_name] = []

        if response_code.startswith('P'):
            continue
        if response_code.startswith('D') or response_code.startswith('F'):
            if server_id not in successful_teams[team_name]:
                team_data[team_name].append([server_id, 20])

        if response_code.startswith('A'):
            if server_id not in successful_teams[team_name]:
                successful_teams[team_name].append(server_id)
            team_data[team_name].append([server_id, elapsed_time])
            continue

    leaderboard = {}
    for team, info in team_data.items():
        leaderboard[team] = [len(successful_teams[team]), 0]
        for server, time in info:
            if server in successful_teams[team]:
                leaderboard[team][1] += time

    leaderboard = sorted(
        leaderboard.items(), key=lambda x: (-x[1][0], x[1][1], x[0]))
    rank = 0
    previous_score = [float('inf'), -1]
    for team, score in leaderboard:
        if score == previous_score:
            print(rank, team, score[0], score[1])
        else:
            rank += 1
            print(rank, team, score[0], score[1])
            previous_score = score
    return 0


if __name__ == "__main__":
    main()
