from collections import defaultdict
from itertools import count

N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]


def make_boundary(table, row, col, d1, d2):
    table[row][col] = 5
    for i in range(1, d1+1):
        table[row+i][col-i] = 5
        table[row+d2+i][col+d2-i] = 5

    for i in range(1, d2+1):
        table[row+i][col+i] = 5
        table[row+d1+i][col-d1+i] = 5

    for i in range(row+1, row+d1+d2):
        start = False
        for j in range(N):
            if table[i][j] == 5:
                if start:
                    break
                else:
                    start = True
            if start:
                table[i][j] = 5


def count_popular(table, popular_dict, r, c, d1, d2):
    for row in range(N):
        for col in range(N):
            if table[row][col] == 5:
                popular_dict[5] += A[row][col]
                continue
            if 0 <= row < r+d1 and 0 <= col <= c:
                popular_dict[1] += A[row][col]
            elif 0 <= row <= r+d2 and c < col < N:
                popular_dict[2] += A[row][col]
            elif r+d1 <= row < N and 0 <= col < c-d1+d2:
                popular_dict[3] += A[row][col]
            elif r+d2 < row < N and c-d1+d2 <= col < N:
                popular_dict[4] += A[row][col]


ans = 9999999999
for d1 in range(1, N):
    for d2 in range(1, N):
        for row in range(N-d1-d2):
            for col in range(d1, N-d2):
                table = [[0]*N for _ in range(N)]
                make_boundary(table, row, col, d1, d2)
                popular_dict = defaultdict(int)
                count_popular(table, popular_dict, row, col, d1, d2)
                vals = list(popular_dict.values())
                ans = min(ans, max(vals)-min(vals))
print(ans)
