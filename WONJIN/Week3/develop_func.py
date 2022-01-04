import math

def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    target_idx = 0
    cnt = 1
    for idx, day in enumerate(days):
        if idx == 0:
            continue
        if day <= days[target_idx]:
            cnt += 1
        else:
            answer.append(cnt)
            target_idx = idx
            cnt = 1
    answer.append(cnt)
    return answer