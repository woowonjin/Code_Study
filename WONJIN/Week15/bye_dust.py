from copy import deepcopy


R, C, T = list(map(int, input().split()))

table = [list(map(int, input().split())) for _ in range(R)]

# cleaner = []
# dusts = []
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

# for i in range(R):
#     for j in range(C):
#         if table[i][j] == -1:
#             cleaner.append([i, j])
#         elif table[i][j] != 0:
#             dusts.append([i, j, table[i][j]])


def diffuse(table, dusts):
    for row, col, amount in dusts:
        new_dust = []
        for m_row, m_col in move:
            n_row = row + m_row
            n_col = col + m_col
            if 0 <= n_row < R and 0 <= n_col < C:
                if table[n_row][n_col] == -1:
                    continue
                new_dust.append([n_row, n_col])
        diffused = amount // 5
        for r, c in new_dust:
            table[r][c] += diffused
        table[row][col] -= diffused * len(new_dust)


def rotate(table, cleaner):
    new_table = [[0]*C for _ in range(R)]

    up_cleaner_row = cleaner[0][0]
    down_cleaner_row = cleaner[1][0]

    new_table[up_cleaner_row][0] = -1
    new_table[down_cleaner_row][0] = -1

    for i in range(R):
        for j in range(C):
            if i == 0 or i == up_cleaner_row or i == down_cleaner_row or i == R-1:
                continue
            elif j == 0 or j == C-1:
                continue
            else:
                new_table[i][j] = table[i][j]

    for col in range(0, C-1):
        if col == 0:
            new_table[up_cleaner_row][col+1] = 0
        else:
            new_table[up_cleaner_row][col+1] = table[up_cleaner_row][col]
    for row in range(up_cleaner_row, 0, -1):
        new_table[row-1][C-1] = table[row][C-1]
    for col in range(C-1, 0, -1):
        new_table[0][col-1] = table[0][col]
    for row in range(0, up_cleaner_row-1):
        new_table[row+1][0] = table[row][0]

    for col in range(0, C-1):
        if col == 0:
            new_table[down_cleaner_row][col+1] = 0
        else:
            new_table[down_cleaner_row][col+1] = table[down_cleaner_row][col]
    for row in range(down_cleaner_row, R-1):
        new_table[row+1][C-1] = table[row][C-1]
    for col in range(C-1, 0, -1):
        new_table[R-1][col-1] = table[R-1][col]

    for row in range(R-1, down_cleaner_row+1, -1):
        new_table[row-1][0] = table[row][0]

    return new_table


for _ in range(T):
    dusts = []
    cleaner = []
    for i in range(R):
        for j in range(C):
            if table[i][j] == -1:
                cleaner.append([i, j])
            elif table[i][j] != 0:
                dusts.append([i, j, table[i][j]])
    diffuse(table, dusts)
    table = rotate(table, cleaner)

ans = 0
for i in range(R):
    for j in range(C):
        if table[i][j] != -1:
            ans += table[i][j]
print(ans)
