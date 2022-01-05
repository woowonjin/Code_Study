from collections import deque

def solution(priorities, location):
    answer = 1
    queue = deque([])
    for idx, priority in enumerate(priorities):
        queue.append([priority, idx])
    
    while queue:
        prior, loc = queue.popleft()
        is_in = False
        for priority, idx in queue:
            if priority > prior:
                print("here")
                is_in = True
                break
        if is_in:
            queue.append([prior, loc])
        else:
            if loc == location:
                break
            answer += 1
    return answer