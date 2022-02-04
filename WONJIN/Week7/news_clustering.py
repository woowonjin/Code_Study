from collections import defaultdict
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_set = []
    str2_set = []
    all_set = set()
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_set.append(str1[i:i+2])
            all_set.add(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_set.append(str2[i:i+2])
            all_set.add(str2[i:i+2])
    
    str1_cnt = defaultdict(int)
    str2_cnt = defaultdict(int)
    
    for char in str1_set:
        str1_cnt[char] += 1
    for char in str2_set:
        str2_cnt[char] += 1
        
    if not all_set:
        return 65536
    union_cnt = 0
    intersection_cnt = 0
    for char in all_set:
        union_cnt += max(str1_cnt[char], str2_cnt[char])
        intersection_cnt += min(str1_cnt[char], str2_cnt[char])
    
    answer = int(intersection_cnt/union_cnt*65536)
    return answer
