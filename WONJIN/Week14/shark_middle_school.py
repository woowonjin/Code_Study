from collections import deque
from hashlib import new
from operator import ne
N, M = list(map(int, input().split()))

table = [list(map(int, input().split())) for _ in range(N)]


def find_max_group_and_remove(table):
    visited = [[False]*N for _ in range(N)]
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    all_groups = []
    for i in range(N):
        for j in range(N):
            if table[i][j] <= 0 or visited[i][j]:
                continue
            queue = deque()
            queue.append([i, j])
            # visited[i][j] = True
            target_num = table[i][j]
            history = []
            history.append([i, j])
            visited[i][j] = True
            while queue:
                row, col = queue.popleft()
                for m_row, m_col in move:
                    n_row = row + m_row
                    n_col = col + m_col
                    if 0 <= n_row < N and 0 <= n_col < N:
                        if table[n_row][n_col] < 0 or visited[n_row][n_col]:
                            continue
                        if table[n_row][n_col] == target_num or table[n_row][n_col] == 0:
                            visited[n_row][n_col] = True
                            queue.append([n_row, n_col])
                            history.append([n_row, n_col])
            rainbow_cnt = 0
            min_row = 99999
            min_col = 99999
            for row, col in history:
                if table[row][col] == 0:
                    rainbow_cnt += 1
                    visited[row][col] = False
                else:
                    if row < min_row:
                        min_row = row
                        min_col = col
                    elif row == min_row:
                        min_col = col
            history.append([rainbow_cnt, min_row, min_col])
            all_groups.append(history)
    if not all_groups:
        return -1, False
    all_groups.sort(key=lambda x: [len(x), x[-1]
                                   [0], x[-1][1], x[-1][2]], reverse=True)
    max_groups = all_groups[0][:-1]
    if len(max_groups) < 2:
        return -1, False
    for row, col in max_groups:
        table[row][col] = -100
    return len(max_groups), True


def gravity(table):
    for col in range(N):
        row = N-2
        while row >= 0:
            if table[row][col] < 0:
                row -= 1
                continue
            # table[row][col] > 0 -> 중력 작용
            target_row = row+1
            if table[target_row][col] >= -1:
                row -= 1
                continue
            while target_row < N:
                if table[target_row][col] < -1:
                    target_row += 1
                else:
                    break
            table[target_row-1][col] = table[row][col]
            table[row][col] = -100
            row -= 1


def turn_table(table):
    new_table = [[-1000]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_table[N-1-j][i] = table[i][j]
    return new_table


answer = 0
while True:
    score, check = find_max_group_and_remove(table)
    gravity(table)
    table = turn_table(table)
    gravity(table)
    # for t in table:
    #     print(t)
    if check:
        answer += score**2
    else:
        break
print(answer)
