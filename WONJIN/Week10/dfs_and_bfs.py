from collections import defaultdict, deque

N, M, V = list(map(int, input().split()))

edges = defaultdict(set)
for _ in range(M):
    v1, v2 = list(map(int, input().split()))
    edges[v1].add(v2)
    edges[v2].add(v1)

bfs_path = []
dfs_path = []
dfs_visited = {key : False for key in range(1, N+1)}
bfs_visited = {key : False for key in range(1, N+1)}

def dfs(node, edges):
    global dfs_path
    global dfs_visited
    if dfs_visited[node]:
        return
    dfs_path.append(node)
    dfs_visited[node] = True
    for n_node in sorted(edges[node]):
        if not dfs_visited[n_node]:
            dfs(n_node, edges)
dfs(V, edges)

queue = deque([V])
while queue:
    node = queue.popleft()
    if bfs_visited[node]:
        continue
    bfs_path.append(node)
    bfs_visited[node] = True
    next_nodes = list(edges[node])
    next_nodes.sort()
    for n_node in next_nodes:
        if not bfs_visited[n_node]:
            queue.append(n_node)
# for node in dfs_path:
#     print(node, end=" ")
# print()
# for node in bfs_path:
#     print(node, end=" ")
# print()
print(*dfs_path)
print(*bfs_path)

