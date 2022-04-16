from collections import deque


N, M, K = list(map(int, input().split()))

table = [list(map(int, input().split())) for _ in range(N)]

dice = [1, 6, 3, 4, 5, 2]  # top, bottom, right, left, front, back
dir_idx = {"top": 0, "bottom": 1, "right": 2, "left": 3, "front": 4, "back": 5}
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
move_idx = 0

row = 0
col = 0


def change_dice(dice, move_idx):
    cur_top = dice[0]
    cur_bottom = dice[1]
    cur_right = dice[2]
    cur_left = dice[3]
    cur_front = dice[4]
    cur_back = dice[5]
    if move_idx == 0:  # right
        dice[dir_idx["right"]] = cur_top
        dice[dir_idx["top"]] = cur_left
        dice[dir_idx["left"]] = cur_bottom
        dice[dir_idx["bottom"]] = cur_right
    elif move_idx == 1:  # bottom
        dice[dir_idx["top"]] = cur_back
        dice[dir_idx["front"]] = cur_top
        dice[dir_idx["bottom"]] = cur_front
        dice[dir_idx["back"]] = cur_bottom
    elif move_idx == 2:  # left
        dice[dir_idx["right"]] = cur_bottom
        dice[dir_idx["top"]] = cur_right
        dice[dir_idx["left"]] = cur_top
        dice[dir_idx["bottom"]] = cur_left
    elif move_idx == 3:  # top
        dice[dir_idx["top"]] = cur_front
        dice[dir_idx["back"]] = cur_top
        dice[dir_idx["bottom"]] = cur_back
        dice[dir_idx["front"]] = cur_bottom


def move_dice(row, col, move_idx):
    n_row = row + moves[move_idx][0]
    n_col = col + moves[move_idx][1]
    if 0 <= n_row < N and 0 <= n_col < M:
        row = n_row
        col = n_col
    else:
        move_idx = (move_idx + 2) % 4
        row += moves[move_idx][0]
        col += moves[move_idx][1]
    return row, col, move_idx


def get_score(row, col):
    cur_val = table[row][col]
    queue = deque()
    queue.append([row, col])
    cnt = 0
    visited = [[False]*M for _ in range(N)]
    visited[row][col] = True
    while queue:
        r, c = queue.popleft()
        cnt += 1
        for m_r, m_c in moves:
            n_r = r + m_r
            n_c = c + m_c
            if 0 <= n_r < N and 0 <= n_c < M:
                if visited[n_r][n_c]:
                    continue
                if table[n_r][n_c] == cur_val:
                    queue.append([n_r, n_c])
                    visited[n_r][n_c] = True

    return cnt*cur_val


def change_direction(row, col, move_idx):
    A = dice[dir_idx["bottom"]]
    B = table[row][col]
    if A == B:
        pass
    elif A > B:
        move_idx = (move_idx + 1) % 4
    else:
        move_idx = move_idx - 1 if move_idx > 0 else 3
    return move_idx


ans = 0
for _ in range(K):
    row, col, move_idx = move_dice(row, col, move_idx)
    change_dice(dice, move_idx)
    ans += get_score(row, col)
    move_idx = change_direction(row, col, move_idx)
print(ans)
