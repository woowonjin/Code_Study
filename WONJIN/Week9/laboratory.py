from itertools import combinations
from copy import deepcopy
from collections import deque
def infect_and_cnt(table, indices_2):
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque(indices_2)
    while queue:
        row, col = queue.popleft()
        for m_row, m_col in move:
            n_row = row + m_row
            n_col = col + m_col
            if 0 <= n_row < len(table) and 0 <= n_col < len(table[0]):
                if table[n_row][n_col] == 0:
                    table[n_row][n_col] = 2
                    queue.append([n_row, n_col])
    cnt = 0
    for row in table:
        for num in row:
            if num == 0:
                cnt += 1
    return cnt

N, M = list(map(int, input().split()))

table = [list(map(int, input().split())) for _ in range(N)]

indices_0 = []
indices_2 = []
for row in range(N):
    for col in range(M):
        if table[row][col] == 0:
            indices_0.append([row, col])
        elif table[row][col] == 2:
            indices_2.append([row, col])

combs = list(combinations(indices_0, 3))

max_cnt = -1
for comb in combs:
    new_table = deepcopy(table)
    for row, col in comb:
        new_table[row][col] = 1
    max_cnt = max(max_cnt, infect_and_cnt(new_table, indices_2))
print(max_cnt)