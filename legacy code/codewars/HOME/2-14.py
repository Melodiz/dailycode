
def sun_angle(time):
    rl_time = int(time[0:2])*60+int(time[3:])
    if rl_time>18*60 or rl_time<6*60:
        return "I don't see the sun!"
    else:
        return 0.25*(rl_time-6*60)


print("Example:")
print(sun_angle("07:00"))

assert sun_angle("07:00") == 15
assert sun_angle("12:15") == 93.75

print("The mission is done! Click 'Check Solution' to earn rewards!")
