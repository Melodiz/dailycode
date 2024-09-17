time_stamps = []
for hour in range(24):
    for minute in range(60):
        for second in range(60):
            time_stamps.append(f"{hour:02}:{minute:02}:{second:02}")

def diff_time(s, t):
    T1 = (int(s[6:8])) + (int(s[3:5]) * 60) + (int(s[0:2]) * 60 * 60)
    T2 = (int(t[6:8])) + (int(t[3:5]) * 60) + (int(t[0:2]) * 60 * 60)
    
    if T2 >= T1:
        return (T2 - T1) // 60
    return (24 * 60 * 60 + T2 - T1) // 60

def convert_time_to_seconds(time_str, start_time=None):
    hours, minutes, seconds = map(int, time_str.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    if start_time is None:
        return total_seconds
    if total_seconds > start_time:
        return (total_seconds - start_time) // 60
    return (total_seconds - start_time + 86400) // 60

from tqdm import tqdm
for i in tqdm(range(len(time_stamps))):
    start_time = convert_time_to_seconds(time_stamps[i])
    row_start_time = time_stamps[i]

    for j in range(i + 1, len(time_stamps)):
        a = diff_time(row_start_time, time_stamps[j])
        b = convert_time_to_seconds(time_stamps[j], start_time)
        assert a == b

print("All test cases passed")