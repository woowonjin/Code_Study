from collections import defaultdict, deque

def bfs(node, edges, visited):
    queue = deque([node])
    flag = True
    while queue:
        v = queue.popleft()
        if visited[v]:
            flag = False
        visited[v] = True
        for n_v in edges[v]:
            if not visited[n_v]:
                queue.append(n_v)
    return flag

cnt = 1
while True:
    n, m = list(map(int, input().split()))
    if n == 0 and m == 0:
        break
    visited = [False for _ in range(n+1)]
    edges = defaultdict(list)
    for _ in range(m):
        v1, v2 = list(map(int, input().split()))
        if v1 != v2:
            edges[v1].append(v2)
            edges[v2].append(v1)
    ans = 0    
    for i in range(1, n+1):
        if visited[i]:
            continue
        if bfs(i, edges, visited):
            ans += 1
    if ans == 0:
        print(f"Case {cnt}: No trees.")
    elif ans == 1:
        print(f"Case {cnt}: There is one tree.")
    else:
        print(f"Case {cnt}: A forest of {ans} trees.")
    cnt += 1