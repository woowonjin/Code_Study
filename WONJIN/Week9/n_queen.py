from collections import deque
def check(row, col, queens):
    for queen in queens:
        if queen[1] == col:
            return False
        if abs(row-queen[0]) == abs(col-queen[1]):
            return False
    return True

N = int(input())
table = [[[0, col]]for col in range(N)]

queue = deque(table)
cnt = 0
while(queue):
    queens = queue.popleft()
    last_row = queens[-1][0]
    if last_row == N-1:
        if len(queens) == N:
            cnt += 1
        continue
    for col in range(N):
        if check(last_row+1, col, queens):
            queue.append(queens+[[last_row+1, col]])
print(cnt)