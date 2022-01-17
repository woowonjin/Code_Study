from collections import defaultdict
# from itertools import combinations
# from functools import reduce

# def solution(clothes):
#     answer = 0
#     wear_dict = defaultdict(int)
#     for cloth, kind in clothes:
#         wear_dict[kind] += 1
    
#     cnt_list = [cnt for _, cnt in wear_dict.items()]
#     for i in range(1, len(cnt_list)+1):
#         combs = list(combinations(cnt_list, i))
#         for comb in combs:
#             cnt = reduce(lambda acc, num: acc*num, comb, 1)
#             answer += cnt
                
#     return answer
def solution(clothes):
    wear_dict = defaultdict(int)
    for cloth, kind in clothes:
        wear_dict[kind] += 1
    answer = 1
    for key, cnt in wear_dict.items():
        answer *= cnt+1 # 안입는 경우 포함
    answer -= 1 # 전체 안입는 경우
    return answer