def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    threshold = min(len(citations), citations[0])
    for h in range(threshold+1):
        cnt = 0
        for idx, citation in enumerate(citations):
            if citation < h:
                break
            cnt += 1
        if h <= cnt:
            answer = max(h, answer)
    return answer