from collections import defaultdict
import heapq

V, E = list(map(int, input().split()))

start = int(input())
inf = 999999999

dist = [inf for _ in range(V+1)]
dist[start] = 0
visited = [False for _ in range(V+1)]
visited[0] = True

edges = defaultdict(list)

for _ in range(E):
    u, v, w = list(map(int, input().split()))
    edges[u].append([w, v])

heap = []
heapq.heappush(heap, [0, start])

while heap:
    weight, u = heapq.heappop(heap)
    if visited[u]:
        continue

    visited[u] = True
    for w, node in edges[u]:
        if not visited[node] and dist[node] > dist[u]+w:
            heapq.heappush(heap, [dist[u]+w, node])
            dist[node] = dist[u]+w

for i in range(1, V+1):
    if dist[i] == inf:
        print("INF")
    else:
        print(dist[i])