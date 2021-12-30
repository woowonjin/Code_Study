def solution(people, limit):
    people.sort()
    answer = 0
    min_idx = 0
    max_idx = len(people)-1
    while min_idx <= max_idx:
        if people[min_idx] + people[max_idx] <= limit:
            min_idx += 1
            max_idx -= 1
        else:
            max_idx -= 1
        answer += 1
        
    return answer