def solution(distance, rocks, n):
    rocks.sort()
    left = 0
    right = distance
    answer = 0
    while left <= right:
        removed_cnt = 0
        mid = (left+right)//2
        criteria = 0
        for rock in rocks:
            if rock-criteria < mid:
                removed_cnt += 1
            else:
                criteria = rock
        if removed_cnt > n:
            right = mid-1
        else:
            left = mid+1
            answer = max(answer, mid)
    
    return answer