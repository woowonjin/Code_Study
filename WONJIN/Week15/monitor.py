from copy import deepcopy

N, M = list(map(int, input().split()))

table = [list(input().split()) for _ in range(N)]

indexes = []

for i in range(N):
    for j in range(M):
        if table[i][j] == "0" or table[i][j] == "6":
            continue
        else:
            indexes.append([i, j])

directions = {"1": [[[1, 0]], [[-1, 0]], [[0, 1]], [[0, -1]]],
              "2": [[[0, 1], [0, -1]], [[1, 0], [-1, 0]]],
              "3": [[[-1, 0], [0, 1]], [[-1, 0], [0, -1]], [[1, 0], [0, -1]], [[1, 0], [0, 1]]],
              "4": [[[0, 1], [-1, 0], [0, -1]], [[-1, 0], [0, -1], [1, 0]], [[0, -1], [1, 0], [0, 1]], [[-1, 0], [0, 1], [1, 0]]],
              "5": [[[0, 1], [1, 0], [-1, 0], [0, -1]]]}

ans = 9999999


def get_side(table):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if table[i][j] == "0":
                cnt += 1
    return cnt


def dfs(idx, table):
    if idx >= len(indexes):
        global ans
        ans = min(ans, get_side(table))
        return
    row, col = indexes[idx][0], indexes[idx][1]
    # print(row, col, idx)
    move = directions[table[row][col]]
    for case in move:
        new_table = deepcopy(table)
        for m_row, m_col in case:
            dist = 1
            while True:
                n_row = row + m_row*dist
                n_col = col + m_col*dist
                if 0 <= n_row < N and 0 <= n_col < M:
                    if new_table[n_row][n_col] == "6":
                        break
                    elif new_table[n_row][n_col] == "0":
                        new_table[n_row][n_col] = "#"
                else:
                    break
                dist += 1
        dfs(idx+1, new_table)


dfs(0, table)
print(ans)
