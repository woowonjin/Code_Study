N = int(input())

meeting_times = []
for _ in range(N):
    meeting = list(map(int, input().split()))
    meeting_times.append(meeting)

meeting_times.sort(key=lambda x : [x[1], x[0]])

answer = 0
last_end = -1
for start, end in meeting_times:
    if start >= last_end:
        answer += 1
        last_end = end
print(answer)