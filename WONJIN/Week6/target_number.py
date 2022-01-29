from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([(numbers[0], 1), (-numbers[0], 1)]) # sum_val, idx
    res = []
    while queue:
        val, idx = queue.popleft()
        if idx == len(numbers)-1:
            res.append(val+numbers[idx])
            res.append(val-numbers[idx])
        else:
            queue.append([val+numbers[idx], idx+1])
            queue.append([val-numbers[idx], idx+1])
    for num in res:
        if num == target:
            answer += 1
    return answer