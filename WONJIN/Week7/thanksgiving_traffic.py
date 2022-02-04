def count(start, times):
    end = start + 1.0
    cnt = 0
    for time in times:
        if time[0] >= end or time[1] < start:
            pass
        else:
            cnt += 1
    # print("start:", start, "end:", end, "cnt:", cnt)
    return cnt

def solution(lines):
    if len(lines) == 1:
        return 1
    times = []
    for line in lines:
        date, end_time, duration = line.split(" ")
        end_hour, end_minute, end_second = end_time.split(":")
        end_hour = int(end_hour)
        end_minute = int(end_minute)
        end_second = float(end_second)
        duration = float(duration[0:-1])
        end_time_second = 60*60*end_hour + 60*end_minute + end_second
        start_time_second = round(end_time_second - duration + 0.001, 3)
        times.append((start_time_second, end_time_second))
    cnt = -1
    for time in times:
        temp1 = count(time[0], times)
        temp2 = count(time[1], times)
        cnt = max(temp1, temp2, cnt)
    answer = cnt
    return answer