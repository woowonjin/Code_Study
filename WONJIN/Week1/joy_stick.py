def get_best(target):
    if target <= "N":
        return ord(target)-ord("A")
    else:
        return ord("Z")-ord(target)+1
    
def get_location(name, idx):
    right_cnt = 0
    right_loc = idx + 1
    left_cnt = 0
    left_loc = idx - 1 if idx != 0 else len(name)-1
    for i in range(idx+1, len(name)):
        if name[i] != "A":
            right_loc = i
            break
        right_cnt += 1
    i = idx-1
    while True:
        if i == -1:
            i = len(name)-1
        if name[i] != "A":
            left_loc = i
            break
        left_cnt += 1
        i -= 1
    if idx < left_loc:
        left_cnt = min(left_cnt, left_loc-idx)
    if idx > right_loc:
        right_cnt = min(right_cnt, idx-right_loc)
    if right_loc >= len(name):
        return left_cnt, left_loc
    if left_cnt < right_cnt:
        return left_cnt, left_loc
    else:
        return right_cnt, right_loc

def solution(name):
    name = [alpha for alpha in name]
    # print(f"original : {name}")
    answer = 0
    idx = 0
    not_A_cnt = 0
    for alpha in name:
        if alpha != "A":
            not_A_cnt += 1
    temp_cnt = 0
    answer += get_best(name[idx])
    if name[idx] != "A":
        temp_cnt += 1
    name[idx] = "A"
    # print(name, answer)
    while temp_cnt < not_A_cnt:
        cnt, loc = get_location(name, idx) # 위치 찾아가는 과정
        answer += cnt+1 # 위치 찾아가는 과정
        answer += get_best(name[loc]) # 문자 바꾸기
        idx = loc
        temp_cnt += 1
        name[idx] = "A"
        # print(name, answer, idx)
    return answer