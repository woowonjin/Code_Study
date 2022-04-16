N, M = list(map(int, input().split()))

table = [list(map(int, input().split())) for _ in range(N)]

move = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

clouds = [[N-2, 0], [N-2, 1], [N-1, 0], [N-1, 1]]
visited = [[False]*N for _ in range(N)]


def move_clouds(d, s, clouds):
    m_row, m_col = move[d][0]*s, move[d][1]*s
    moved_clouds = []
    for row, col in clouds:
        n_row = row + m_row
        n_col = col + m_col
        if n_row < 0:
            row_q = n_row//N
            n_row += N*abs(row_q)
        elif n_row >= N:
            row_q = n_row//N
            n_row -= N*row_q
        if n_col < 0:
            col_q = n_col//N
            n_col += N*abs(col_q)
        elif n_col >= N:
            col_q = n_col//N
            n_col -= N*col_q
        moved_clouds.append([n_row, n_col])
        visited[n_row][n_col] = True
    return moved_clouds


def rain(clouds, table):
    for row, col in clouds:
        table[row][col] += 1


def copy_magic(clouds, table):
    moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for row, col in clouds:
        cnt = 0
        for m_row, m_col in moves:
            n_row = row + m_row
            n_col = col + m_col
            if 0 <= n_row < N and 0 <= n_col < N:
                if table[n_row][n_col] > 0:
                    cnt += 1
        table[row][col] += cnt


def make_clouds(clouds, table):
    new_clouds = []
    for i in range(N):
        for j in range(N):
            if table[i][j] >= 2 and not visited[i][j]:
                table[i][j] -= 2
                new_clouds.append([i, j])
            visited[i][j] = False
    return new_clouds


for _ in range(M):
    d, s = list(map(int, input().split()))
    d -= 1
    clouds = move_clouds(d, s, clouds)
    rain(clouds, table)
    copy_magic(clouds, table)
    clouds = make_clouds(clouds, table)

ans = 0
for i in range(N):
    for j in range(N):
        ans += table[i][j]
print(ans)
