
from collections import deque
def solution(n, results):
    answer = 0
    lose_dict = {} # key is loser, vals is winners
    win_dict = {} # key is winner
    for i in range(1, n+1):
        lose_dict[i] = []
        win_dict[i] = []
    
    for winner, loser in results:
        lose_dict[loser].append(winner)
        win_dict[winner].append(loser)
    
    for i in range(1, n+1):
        loser_queue = deque(lose_dict[i])
        winner_queue = deque(win_dict[i])
        while loser_queue:
            target = loser_queue.popleft()
            for n_target in lose_dict[target]:
                if not n_target in lose_dict[i]:
                    lose_dict[i].append(n_target)
                    loser_queue.append(n_target)
        while winner_queue:
            target = winner_queue.popleft()
            for n_target in win_dict[target]:
                if not n_target in win_dict[i]:
                    win_dict[i].append(n_target)
                    winner_queue.append(n_target)

    for i in range(1, n+1):
        cnt = len(win_dict[i])+len(lose_dict[i])
        if cnt == n-1:
            answer += 1
    return answer

# print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]), 2)
# print(solution(7, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [5,6], [6,7]]), 4)
# print(solution(6, [[1,2], [2,3], [3,4], [4,5], [5,6]]), 6)
# print(solution(5, [[1, 4], [4, 2], [2, 5], [5, 3]]), 5)
# print(solution(5, [[3, 5], [4, 2], [4, 5], [5, 1], [5, 2]]), 1)
# print(solution(3, [[1,2],[1,3]]), 1)
# print(solution(6, [[1,6],[2,6],[3,6],[4,6]]), 0)
# print(solution(8, [[1,2],[3,4],[5,6],[7,8]]),0)
# print(solution(9, [[1,2],[1,3],[1,4],[1,5],[6,1],[7,1],[8,1],[9,1]]), 1)
# print(solution(6, [[1,2],[2,3],[3,4],[4,5],[5,6],[2,4],[2,6]]), 6)
# print(solution(4, [[4,3],[4,2],[3,2],[3,1],[4,1], [2,1]]), 4)
# print(solution(3,[[3,2],[3,1]]), 1)
# print(solution(4, [[1,2],[1,3],[3,4]]), 1)