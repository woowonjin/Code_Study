def solution(n, times):
    left, right = 1, 1000000000000000009
    answer = 1000000000000000009
    while left <= right:
        mid = (left+right)//2
        
        done_person_num = sum([mid//time for time in times])
        
        if done_person_num >= n:
            right = mid-1
            answer = min(mid, answer)
        else:
            left = mid+1
    return answer