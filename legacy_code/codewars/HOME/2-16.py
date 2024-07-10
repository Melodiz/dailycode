def date_time(time):
    minutes = 'minutes'
    if time[14:] == '01':
        minutes = "minute"
    hours = 'hours'
    if time[11:13] == '01':
        hours = 'hour'

    mont = ['0','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    return f'{int(time[0:2])} {mont[int(time[3:5])]} {time[6:10]} year {int(time[11:13])} {hours} {int(time[14:])} {minutes}'


print("Example:")
print(date_time("01.01.2000 00:00"))

assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
assert date_time("09.05.1945 06:07") == "9 May 1945 year 6 hours 7 minutes"
assert date_time('11.04.1812 01:01') == '11 April 1812 year 1 hour 1 minute'

print("The mission is done! Click 'Check Solution' to earn rewards!")


