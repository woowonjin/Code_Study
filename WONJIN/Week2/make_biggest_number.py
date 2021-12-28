def solution(number, k):
    len_num = len(number)-k
    answer = ''
    start_idx = 0
    while len_num > 0:
        max_num = -1
        max_idx = -1
        for i in range(start_idx, len(number)-len_num+1):
            if int(number[i]) > max_num:
                max_num = int(number[i])
                max_idx = i
            if max_num == 9:
                break
        answer += number[max_idx]
        start_idx = max_idx+1 if max_idx+1 < len(number) else len(number)-1
        len_num -= 1
            
    return answer