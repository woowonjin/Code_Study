from collections import defaultdict

def solution(genres, plays):
    res_dict = defaultdict(list)
    res_cnt = defaultdict(int)
    answer = []
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        res_dict[genre].append([idx, play])
        res_cnt[genre] += play
    for key, val in res_dict.items():
        val.sort(key=lambda x : x[1] ,reverse=True)
    res_list = []
    for key, val in res_cnt.items():
        res_list.append([key, val])
    res_list.sort(key=lambda x : x[1], reverse=True)
    for genre, _ in res_list:
        if len(res_dict[genre]) < 2:
            answer.append(res_dict[genre][0][0])
        else:
            answer.append(res_dict[genre][0][0])
            answer.append(res_dict[genre][1][0])
    
    return answer