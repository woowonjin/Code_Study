from collections import deque
N = int(input())

table = [list(map(int, input().split())) for _ in range(N)]

shark_pos = None
for i in range(N):
    for j in range(N):
        if table[i][j] == 9:
            shark_pos = [i, j]
            break


def bfs(shark_size, shark_pos):
    visited = [[False]*N for _ in range(N)]
    dist = [[0]*N for _ in range(N)]
    queue = deque()
    queue.append(shark_pos)
    visited[shark_pos[0]][shark_pos[1]] = True
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    candidates = []
    while queue:
        row, col = queue.popleft()
        for m_row, m_col in move:
            n_row = row + m_row
            n_col = col + m_col
            if 0 <= n_row < N and 0 <= n_col < N:
                if visited[n_row][n_col]:
                    continue
                if table[n_row][n_col] <= shark_size:
                    queue.append([n_row, n_col])
                    visited[n_row][n_col] = True
                    dist[n_row][n_col] = dist[row][col] + 1
                    if table[n_row][n_col] < shark_size and table[n_row][n_col] != 0:
                        candidates.append([dist[n_row][n_col], n_row, n_col])
    return candidates


time = 0
shark_size = 2
cnt = 0
table[shark_pos[0]][shark_pos[1]] = 0
while True:
    candidates = bfs(shark_size, shark_pos)
    if not candidates:
        break

    candidates.sort(key=lambda x: [x[0], x[1], x[2]])
    dist, row, col = candidates[0]
    table[row][col] = 0
    time += dist
    shark_pos = [row, col]
    cnt += 1
    if cnt == shark_size:
        cnt = 0
        shark_size += 1

print(time)
