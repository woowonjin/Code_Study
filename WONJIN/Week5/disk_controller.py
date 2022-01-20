import heapq
from collections import deque

def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x : x[0])
    cnt = 0
    heap = []
    queue = deque(jobs)
    while queue or heap:
        if queue:
            while queue and queue[0][0] <= cnt:
                start, duration = queue.popleft()
                heapq.heappush(heap, [duration, start])
        if heap:
            duration, start = heapq.heappop(heap)
            cnt += duration
            answer += cnt - start
            continue
        cnt += 1
    answer = answer // len(jobs)
    return answer

print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]), 74)
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]), 72)