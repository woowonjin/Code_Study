def solution(dartResult):
    answer = 0
    res_list = []
    target_num = 99999
    num_cnt = 0
    dartResult = dartResult.replace("10", "k")
    for char in dartResult:
        if char.isdigit() or char == "k":
            if target_num != 99999:
                res_list.append(target_num)
            if char == "k":
                target_num = 10
            else:
                target_num = int(char)
            num_cnt += 1
        else:
            if char == "S":
                pass
            elif char == "D":
                target_num = target_num**2
            elif char == "T":
                target_num = target_num**3
            elif char == "*":
                if num_cnt != 1:
                    res_list[num_cnt-2] *= 2
                target_num *= 2
            elif char == "#":
                target_num *= -1
    
    res_list.append(target_num)
    answer = sum(res_list)
    return answer