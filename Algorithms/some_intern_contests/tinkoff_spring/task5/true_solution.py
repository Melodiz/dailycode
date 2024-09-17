def diff_time(s, t):
    T1 = (int(s[6:8])) + (int(s[3:5]) * 60) + (int(s[0:2]) * 60 * 60)
    T2 = (int(t[6:8])) + (int(t[3:5]) * 60) + (int(t[0:2]) * 60 * 60)

    if T2 >= T1:
        return (T2 - T1)
    return (24 * 60 * 60 + T2 - T1) // 60


def main():
    start_time = input().strip()
    n = int(input().strip())

    cannot_solve = {}
    teams = {}

    for _ in range(n):
        name, time, problem, type = input().strip().split()
        if name not in teams:
            teams[name] = [0, 0]
        if type == "DENIED" or type == "FORBIDEN":
            cannot_solve[(name, problem)] = cannot_solve.get(
                (name, problem), 0) + 1
        elif type == "ACCESSED":
            teams[name][0] += 1
            teams[name][1] += diff_time(start_time, time)//60 + \
                20 * cannot_solve.get((name, problem), 0)

    leader_board = []
    for key, value in teams.items():
        leader_board.append(((-value[0], value[1]), key))

    leader_board.sort()
    place = 1
    for i in range(len(leader_board)):
        if i > 0 and (leader_board[i - 1][0] != leader_board[i][0]):
            place += 1
        print(place, leader_board[i][1], -leader_board[i][0][0], leader_board[i][0][1])


if __name__ == "__main__":
    main()
