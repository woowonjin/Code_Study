from collections import defaultdict

N, K = list(map(int, input().split()))

table = [list(map(int, input().split()))
         for _ in range(N)]  # 0 : 흰색, 1 : 빨간색, 2 : 파란색

infos = [[[] for _ in range(N)] for _ in range(N)]

horses = [list(map(int, input().split())) for _ in range(K)]

for idx, horse in enumerate(horses):
    horse[0] -= 1
    horse[1] -= 1
    infos[horse[0]][horse[1]].append(idx)

moves = {1: [0, 1], 2: [0, -1], 3: [-1, 0], 4: [1, 0]}


def move_horses(horses, infos):
    for horse_id, horse in enumerate(horses):
        row, col, move_dir = horse
        m_row, m_col = moves[move_dir]
        n_row = row + m_row
        n_col = col + m_col
        color = None
        if 0 <= n_row < N and 0 <= n_col < N:
            color = table[n_row][n_col]
        else:
            color = 2
        if color == 0:
            idx = infos[row][col].index(horse_id)
            temp_info = infos[row][col][idx:]
            for id in temp_info:
                horses[id] = [n_row, n_col, horses[id][2]]
            infos[n_row][n_col] += temp_info
            infos[row][col] = infos[row][col][:idx]
        elif color == 1:
            idx = infos[row][col].index(horse_id)
            temp_info = infos[row][col][idx:]
            for id in temp_info:
                horses[id] = [n_row, n_col, horses[id][2]]
            infos[n_row][n_col] += infos[row][col][idx:][::-1]
            infos[row][col] = infos[row][col][:idx]
        elif color == 2:
            if move_dir % 2 == 0:
                horse[2] -= 1
            else:
                horse[2] += 1
            m_row *= -1
            m_col *= -1
            n_row = row + m_row
            n_col = col + m_col
            if 0 <= n_row < N and 0 <= n_col < N:
                color = table[n_row][n_col]
            else:
                color = 2

            if color == 2:
                n_row = row
                n_col = col
                horses[horse_id] = [n_row, n_col, horse[2]]
                continue
            elif color == 0:
                idx = infos[row][col].index(horse_id)
                temp_info = infos[row][col][idx:]
                for id in temp_info:
                    horses[id] = [n_row, n_col, horses[id][2]]
                infos[n_row][n_col] += infos[row][col][idx:]
                infos[row][col] = infos[row][col][:idx]
                horses[horse_id] = [n_row, n_col, horse[2]]
            elif color == 1:
                idx = infos[row][col].index(horse_id)
                temp_info = infos[row][col][idx:]
                for id in temp_info:
                    horses[id] = [n_row, n_col, horses[id][2]]
                infos[n_row][n_col] += temp_info[::-1]
                infos[row][col] = infos[row][col][:idx]
                horses[horse_id] = [n_row, n_col, horse[2]]
        if check(horses):
            return True
    return False


def check(horses):
    cnt_dict = defaultdict(int)
    for horse in horses:
        key = tuple(horse[:2])
        cnt_dict[key] += 1
        if cnt_dict[key] >= 4:
            return True
    return False


cnt = 0
while cnt <= 1000:
    cnt += 1
    is_true = move_horses(horses, infos)
    if is_true:
        break

if cnt > 1000:
    print(-1)
else:
    print(cnt)
