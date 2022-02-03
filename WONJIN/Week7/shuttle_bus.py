def solution(n, t, m, timetable):
    times = []
    for time in timetable:
        temp = time.split(":")
        hour = int(temp[0])
        minute = int(temp[1])
        times.append(60*hour + minute)

    times.sort()
    answer = ''
    idx = 0
    for num_of_bus in range(n-1):
        temp_idx = idx
        bus_time = 540 + num_of_bus*t
        cnt = 0
        for i in range(temp_idx, len(times)):
            if cnt >= m:
                break
            if times[i] <= bus_time:
                idx += 1
                cnt += 1
            else:
                break
    temp_cnt = 0
    for i in range(idx, len(times)):
        if times[i] <= 540 + (n-1)*t:
            temp_cnt += 1
        else:
            break
    if temp_cnt >= m:
        time = times[idx+m-1] - 1
        hour = int(time/60)
        minute = int(time%60)
        if hour < 10:
            answer += "0" + str(hour) + ":"
        else:
            answer += str(hour) + ":"
        if minute < 10:
            answer += "0" + str(minute)
        else:
            answer += str(minute)
    else:
        time = 540 + (n-1)*t
        hour = int(time/60)
        minute = int(time%60)
        if hour < 10:
            answer += "0" + str(hour) + ":"
        else:
            answer += str(hour) + ":"
        if minute < 10:
            answer += "0" + str(minute)
        else:
            answer += str(minute)
    return answer