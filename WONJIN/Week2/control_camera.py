def solution(routes):
    routes.sort(key=lambda x : (x[0], x[1]))
    target = None
    answer = 0
    for route in routes:
        if not target:
            target = route
            answer += 1
            continue
        if target[0] <= route[0] <= target[1]:
            target[0] = max(target[0], route[0])
            target[1] = min(target[1], route[1])
        else:
            target = route
            answer += 1
    return answer