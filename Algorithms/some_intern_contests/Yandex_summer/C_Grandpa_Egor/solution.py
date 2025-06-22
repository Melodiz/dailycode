
def main():
    c = int(input())

    homes = {}
    for _ in range(c):
        line = input().split()
        city_name, num_rooms = line[0], int(line[1])
        
        homes[city_name] = []
        for _ in range(num_rooms):
            room_line = input().split()
            schedule, room_name = room_line[0], room_line[1]
            homes[city_name].append({'name': room_name, 'schedule': schedule})

    m = int(input())

    for _ in range(m):
        query_line = input().split()
        
        cities = query_line[1:]

        found_solution = False
        solution_rooms = []

        for t in range(24):
            possible_at_this_time = True
            current_rooms_for_t = []

            for city in cities:
                found_room_in_city = False
                if city in homes:
                    for room in homes[city]:
                        if room['schedule'][t] == '.':
                            current_rooms_for_t.append(room['name'])
                            found_room_in_city = True
                            break
                
                if not found_room_in_city:
                    possible_at_this_time = False
                    break

            if possible_at_this_time:
                solution_rooms = current_rooms_for_t
                found_solution = True
                break

        if found_solution:
            print("Yes", *solution_rooms)
        else:
            print("No")

if __name__ == "__main__":
    main()