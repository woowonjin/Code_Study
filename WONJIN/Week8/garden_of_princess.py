N = int(input())

dates = []

days_per_month = {
    0: 0,
    1: 31,
    2: 59,
    3: 90,
    4: 120,
    5: 151,
    6: 181,
    7: 212,
    8: 243,
    9: 273,
    10: 304,
    11: 334,
    12: 365
}

start_criteria = 60
end_criteria = 334

for _ in range(N):
    start_month, start_day, end_month, end_day = list(map(int, input().split()))
    start_days = days_per_month[start_month-1]+start_day
    end_days = days_per_month[end_month-1]+end_day
    dates.append([start_days, end_days])

dates.sort(key=lambda x : x[0])

now_start = 0
now_end = 60
target = []
cnt = 0
idx = 0
while idx < len(dates):
    if now_end > end_criteria:
        break

    start, end = dates[idx]
    if now_start <= start <= now_end:
        target.append([start, end])
        idx += 1
    else:
        if not target:
            break
        now_start, now_end = sorted(target, key=lambda x : x[1])[-1]
        target = []
        cnt += 1
if target:
    now_start, now_end = sorted(target, key=lambda x : x[1])[-1]
    cnt += 1
if now_end > end_criteria:
    print(cnt)
else:
    print(0)