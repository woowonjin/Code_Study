def solution(n, costs):
    answer = 0
    visited = [False for _ in range(n)]
    visited[0] = True
    costs.sort(key=lambda x : x[2])
    while not all(visited):
        for node1, node2, dist in costs:
            if visited[node1] and not visited[node2]:
                visited[node2] = True
                answer += dist
                break
            elif not visited[node1] and visited[node2]:
                visited[node1] = True
                answer += dist
                break
            
    return answer