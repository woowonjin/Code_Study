# v1
# from collections import deque

# M, N = list(map(int, input().split()))

# hills = []

# for _ in range(M):
#     line = list(map(int, input().split()))
#     hills.append(line)
# move = [(0, 1), (0, -1), (1, 0), (0, -1)]
# queue = deque([[(0, 0), []]])
# cnt = 0
# history = []
# while queue:
#     (y, x), visited = queue.popleft()
#     current_height = hills[y][x]
#     if y == M-1 and x == N-1:
#         history.append(visited)
#         continue
#     for m_y, m_x in move:
#         n_y = y + m_y
#         n_x = x + m_x
#         if 0 <= n_x < N and 0 <= n_y < M and not (n_y, n_x) in visited:
#             if current_height > hills[n_y][n_x]:
#                 queue.append([(n_y, n_x), visited+[(y, x)]])
# history = set(list(map(tuple, history)))
# print(len(history))

# v2
# from collections import defaultdict
# M, N = list(map(int, input().split()))
# table = []
# for _ in range(M):
#     line = list(map(int, input().split()))
#     table.append(line)

# cnt_dict = defaultdict(list)
# cnt_dict[0] = [[0,0]]
# cnt = 1
# move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# ans = 0
# while True:
#     if not cnt_dict[cnt-1]:
#         break
#     res = []
#     for row, col in cnt_dict[cnt-1]:
#         for m_row, m_col in move:
#             n_row = row + m_row
#             n_col = col + m_col
#             if 0 <= n_row < M and 0 <= n_col < N:
#                 if table[n_row][n_col] < table[row][col]:
#                     res.append([n_row, n_col])
#     cnt_dict[cnt] = res
#     cnt += 1
#     for row, col in res:
#         if row == M-1 and col == N-1:
#             ans += 1
#     cnt_dict.pop(cnt-2)
# print(ans)

#v3
import heapq

M, N = list(map(int, input().split()))
table = []
for _ in range(M):
    line = list(map(int, input().split()))
    table.append(line)
dp = [[0 for _ in range(N)] for _ in range(M)]
dp[0][0] = 1
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
heap = [[-table[0][0], 0, 0]]
while heap:
    height, row, col = heapq.heappop(heap)
    for m_row, m_col in move:
        n_row = row + m_row
        n_col = col + m_col
        if 0 <= n_row < M and 0 <= n_col < N:
            if table[n_row][n_col] < table[row][col]:
                if dp[n_row][n_col] == 0:
                    heapq.heappush(heap, [-table[n_row][n_col], n_row, n_col])
                dp[n_row][n_col] += dp[row][col]
print(dp[M-1][N-1])
