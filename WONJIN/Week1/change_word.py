from collections import deque
def check(begin, words):
    targets = []
    for word in words:
        diff_cnt = 0
        for i in range(len(begin)):
            if diff_cnt > 1:
                break
            if begin[i] != word[i]:
                diff_cnt += 1
        if diff_cnt == 1:
            targets.append(word)
    return targets

def solution(begin, target, words):
    answer = 99999
    queue = deque([[begin, 0, []]])
    while queue:
        word, cnt, used = queue.popleft()
        # print(word, cnt, used)
        used.append(word)
        if word == target:
            answer = min(answer, cnt)
        else:
            target_list = check(word, words)
            for target_word in target_list:
                if not target_word in used:
                    queue.append([target_word, cnt+1, used])
    if answer == 99999:
        return 0
    return answer