from collections import deque
N, L, R = list(map(int, input().split()))

table = [list(map(int, input().split())) for _ in range(N)]

move = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def migration(table):
    visited = [[False]*N for _ in range(N)]
    boundaries = []
    populars = []
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            boundary = []
            queue = deque()
            queue.append([i, j])
            visited[i][j] = True
            boundary.append([i, j])
            popular = table[i][j]
            while queue:
                row, col = queue.popleft()
                for m_row, m_col in move:
                    n_row = row + m_row
                    n_col = col + m_col
                    if 0 <= n_row < N and 0 <= n_col < N:
                        if visited[n_row][n_col]:
                            continue
                        if L <= abs(table[row][col]-table[n_row][n_col]) <= R:
                            queue.append([n_row, n_col])
                            visited[n_row][n_col] = True
                            boundary.append([n_row, n_col])
                            popular += table[n_row][n_col]
            boundaries.append(boundary)
            populars.append(popular)
    if len(populars) == N**2:
        return False
    for boundary, popular in zip(boundaries, populars):
        common_popular = popular // len(boundary)
        for row, col in boundary:
            table[row][col] = common_popular
    return True


ans = 0
while True:
    # for t in table:
    #     print(t)
    # print("="*100)
    check = migration(table)
    if not check:
        break
    ans += 1
print(ans)
