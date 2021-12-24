from collections import deque
def solution(tickets):
    ticket_used = [False for _ in range(len(tickets))]
    queue = deque([["ICN", ["ICN"], ticket_used]]) # from, used, route
    answer = []
    while queue:
        node, route, used = queue.popleft()
        if all(used):
            answer.append(route)
        for idx, ticket in enumerate(tickets):
            if not used[idx] and ticket[0] == node:
                temp_used = used[:]
                temp_used[idx] = True
                queue.append([ticket[1], route+[ticket[1]], temp_used])
    answer.sort()
    return answer[0]