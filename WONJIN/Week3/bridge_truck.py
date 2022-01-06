from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque([])
    on_bridge_weight = 0
    answer = 0
    for idx, truck_weight in enumerate(truck_weights):
        if queue:
            if queue[0][1] == 0:
                first_weight, _ = queue.popleft()
                on_bridge_weight -= first_weight
        if on_bridge_weight + truck_weight <= weight:
            for i in range(len(queue)):
                queue[i][1] -= 1
            answer += 1
            on_bridge_weight += truck_weight
            queue.append([truck_weight, bridge_length])
        else:
            while not (on_bridge_weight + truck_weight <= weight):
                first_weight, left_len = queue.popleft()
                on_bridge_weight -= first_weight
                answer += left_len
                for i in range(len(queue)):
                    queue[i][1] -= left_len
            on_bridge_weight += truck_weight
            queue.append([truck_weight, bridge_length])

    if queue:
        target_len = -1
        while queue:
            first_weight, left_len = queue.popleft()
            if target_len == -1:
                target_len = left_len
                answer += left_len
            else:
                answer += left_len - target_len
                target_len = left_len
        return answer
    else:   
        return answer
