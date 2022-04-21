from collections import deque

N, M, T = list(map(int, input().split()))

disk = [list(map(int, input().split())) for _ in range(N)]


def rotate_disk(disk, idx, d, k):
    k %= M
    target = disk[idx]
    if d == 0:  # clockwise
        disk[idx] = target[M-k:] + target[:M-k]
    else:
        disk[idx] = target[k:] + target[:k]


def bfs(disk):
    result = []
    visited = [[False]*M for _ in range(N)]
    for row in range(N):
        for col in range(M):
            if visited[row][col] or disk[row][col] == 0:
                continue
            queue = deque()
            history = []
            queue.append([row, col])
            visited[row][col] = True
            while queue:
                r, c = queue.popleft()
                history.append([r, c])
                n_pos = []
                if c == 0:
                    n_pos += [(r, 1), (r, M-1)]
                elif c == M-1:
                    n_pos += [(r, 0), (r, c-1)]
                else:
                    n_pos += [(r, c-1), (r, c+1)]

                if r == 0:
                    n_pos += [(r+1, c)]
                elif r == N-1:
                    n_pos += [(r-1, c)]
                else:
                    n_pos += [(r-1, c), (r+1, c)]

                for n_row, n_col in n_pos:
                    if visited[n_row][n_col]:
                        continue
                    if disk[n_row][n_col] == 0:
                        continue
                    if disk[n_row][n_col] == disk[row][col]:
                        queue.append([n_row, n_col])
                        visited[n_row][n_col] = True
            result.append(history)
    targets = []
    for res in result:
        if len(res) > 1:
            targets.append(res)
    return targets


def remove(disk, targets):
    for target in targets:
        for row, col in target:
            disk[row][col] = 0


def change(disk):
    cnt = 0
    sum_ = 0
    for row in range(N):
        for col in range(M):
            if disk[row][col] != 0:
                cnt += 1
                sum_ += disk[row][col]
    avg = float(sum_ / cnt)
    for row in range(N):
        for col in range(M):
            if disk[row][col] == 0:
                continue
            if disk[row][col] > avg:
                disk[row][col] -= 1
            elif disk[row][col] < avg:
                disk[row][col] += 1


def check(disk):
    for row in range(N):
        for col in range(M):
            if disk[row][col] != 0:
                return True
    return False


for _ in range(T):
    x, d, k = list(map(int, input().split()))
    rotate_list = []
    for i in range(1, N//x+1):
        rotate_list.append(i*x-1)
    for idx in rotate_list:
        rotate_disk(disk, idx, d, k)
    # for d in disk:
    #     print(d)
    # print()
    targets = bfs(disk)
    if not check(disk):
        break
    if targets:
        remove(disk, targets)
    else:
        change(disk)
    # for d in disk:
    #     print(d)
    # print("="*100)
print(sum([sum(row) for row in disk]))
