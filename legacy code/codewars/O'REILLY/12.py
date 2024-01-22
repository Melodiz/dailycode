def time_converter(time):
    day_part = time[time.find('.')-1]
    hours = ''
    
    if day_part == 'a':
        hours = '0'+str(int(time[:time.find(':')]))
        if hours == '012':hours='00'
        
    else:
        hours = (int(time[:time.find(':')])+12)
        if hours >=24:hours-=12
    
    minutes = time[time.find(':'):time.find(' ')]

    return(f'{str(hours)}{minutes}')

if __name__ == "__main__":
    print("Example:")
    print(time_converter("12:30 p.m."))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter("12:30 p.m.") == "12:30"
    assert time_converter("9:00 a.m.") == "09:00"
    assert time_converter("11:15 p.m.") == "23:15"
    print("Coding complete? Click 'Check' to earn cool rewards!")
