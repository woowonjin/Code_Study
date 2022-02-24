from collections import deque

N, M = list(map(int, input().split()))

maze = [input() for _ in range(N)]
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

queue = deque([[0, 0, 1]])
dist = [[99999]*M for _ in range(N)]
dist[0][0] = 1
while queue:
    row, col, cnt = queue.popleft()
    for m_row, m_col in move:
        n_row = row + m_row
        n_col = col + m_col
        if 0 <= n_row < N and 0 <= n_col < M:
            if maze[n_row][n_col] == "1" and dist[n_row][n_col] == 99999:
                queue.append([n_row, n_col, cnt+1])
            dist[n_row][n_col] = min(dist[n_row][n_col], dist[row][col]+1)
print(dist[N-1][M-1])