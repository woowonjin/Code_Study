from collections import deque

def solution(n, computers):
    visited = [False for _ in range(n)]
    queue = deque([0])
    answer = 1
    while not all(visited):
        if not queue: # queue가 비었을떄
            for node, already_visited in enumerate(visited):
                if not already_visited:
                    queue.append(node)
                    answer += 1
                    break
        else:
            node = queue.popleft()
            visited[node] = True
            for computer_node, is_connected in enumerate(computers[node]):
                if is_connected and not visited[computer_node]:
                    queue.append(computer_node)
        
    return answer