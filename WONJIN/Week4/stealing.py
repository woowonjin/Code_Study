def solution(money):
    answer = 0
    dp_1 = {}
    dp_2 = {}
    for idx in range(len(money)-1):
        if idx == 0 or idx == 1:
            dp_1[idx] = money[idx]
        elif idx == 2:
            dp_1[idx] = max(dp_1[idx-2]+money[idx], dp_1[idx-1])
        else:
            dp_1[idx] = max(dp_1[idx-2]+money[idx], dp_1[idx-1], dp_1[idx-3]+money[idx])
    
    for idx in range(1, len(money)):
        if idx == 1 or idx == 2:
            dp_2[idx] = money[idx]
        elif idx == 3:
            dp_2[idx] = max(dp_2[idx-2]+money[idx], dp_2[idx-1])
        else:
            dp_2[idx] = max(dp_2[idx-2]+money[idx], dp_2[idx-1], dp_2[idx-3]+money[idx])
    
    answer = max(dp_1[len(money)-2], dp_2[len(money)-1])
    
    return answer


print(solution([1, 1, 4, 1, 4]), 8)
print(solution([1000, 0, 0, 1000, 0, 0, 1000, 0, 0, 1000]), 3000)
print(solution([1000, 1, 0, 1, 2, 1000, 0]), 2000)
print(solution([1000, 0, 0, 0, 0, 1000, 0, 0, 0, 0, 0, 1000]), 2000)
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 30)
print(solution([0, 0, 0, 0, 100, 0, 0, 100, 0, 0, 1, 1]), 201)
print(solution([11, 0, 2, 5, 100, 100, 85, 1]), 198)
print(solution([1, 2, 3]), 3)

