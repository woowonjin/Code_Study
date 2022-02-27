from collections import defaultdict, deque

N, M = list(map(int, input().split()))

dists = defaultdict(list)
for _ in range(M):
    v1, v2, d = list(map(int, input().split()))
    dists[v1].append([v2, d])
    dists[v2].append([v1, d])

start, end = list(map(int, input().split()))

def bfs(weight):
    queue = deque([start])
    visited = [start]
    while queue:
        node = queue.popleft()
        if end == node:
            return True
        for v, d in dists[node]:
            if not v in visited and weight <= d:
                visited.append(v)
                queue.append(v)
    return False

min_val, max_val = 1, 1000000000
ans = min_val
while min_val <= max_val:
    mid = (min_val + max_val) // 2
    if bfs(mid):
        ans = mid
        min_val = mid + 1
    else:
        max_val = mid - 1
print(ans)