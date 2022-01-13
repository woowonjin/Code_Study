from collections import deque

def solution(n, edge):
    answer = 0
    node_dict = {}
    for i in range(n+1):
        node_dict[i] = []
    for node1, node2 in edge:
        node_dict[node1].append(node2)
        node_dict[node2].append(node1)
    visited = [False for _ in range(n+1)]
    visited[0] = True
    visited[1] = True
    dist = [9999999 for _ in range(n+1)]
    dist[0] = -1
    dist[1] = 0
    queue = deque([1])
    while not all(visited):
        node = queue.popleft()
        for vertex in node_dict[node]:
            if not visited[vertex]:
                visited[vertex] = True
                dist[vertex] = min(dist[vertex], dist[node]+1)
                queue.append(vertex)
    max_val = max(dist)
    for val in dist:
        if val == max_val:
            answer += 1
    return answer