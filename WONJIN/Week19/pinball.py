from collections import deque, defaultdict

T = int(input())

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 0: 상, 1: 하, 2: 좌, 3: 우

block_1 = [1, 3, 0, 2]  # 하, 우, 상, 좌
block_2 = [3, 0, 1, 2]  # 우, 상, 하, 좌
block_3 = [2, 0, 3, 1]  # 좌, 상, 우, 하
block_4 = [1, 2, 3, 0]  # 하, 좌, 우, 상
block_5 = [1, 0, 3, 2]  # 하, 상, 우, 좌

blocks = {1: block_1, 2: block_2, 3: block_3, 4: block_4, 5: block_5}


def get_score(table, row, col, direction, wormholes):
    score = 0
    start_pos = [row, col]
    start_direction = direction
    is_first = True
    while True:
        if start_pos == [row, col] and not is_first:
            return score
        if table[row][col] == -1:
            return score
        is_first = False
        m_row, m_col = directions[direction]
        n_row = row + m_row
        n_col = col + m_col
        # print(
        #     f"start_pos : {start_pos}, start_direction: {start_direction}, pos : {[row, col]}, direction : {direction}, score: {score}")
        if 0 <= n_row < N and 0 <= n_col < N:
            if table[n_row][n_col] == 0 or table[n_row][n_col] == -1:
                row = n_row
                col = n_col
            elif 1 <= table[n_row][n_col] <= 5:  # block
                block_change_direction = blocks[table[n_row][n_col]]
                new_direction = block_change_direction[direction]
                row = n_row
                col = n_col
                direction = new_direction
                score += 1
            elif 6 <= table[n_row][n_col] <= 10:  # wormholes
                wormhole_pair = wormholes[table[n_row][n_col]]
                if wormhole_pair[0] == [n_row, n_col]:
                    another_one = wormhole_pair[1]
                else:
                    another_one = wormhole_pair[0]
                row = another_one[0]
                col = another_one[1]

        else:
            if direction % 2 == 0:
                direction += 1
            else:
                direction -= 1
            score += 1
            if table[row][col] == 0:
                pass
            elif 1 <= table[row][col] <= 5:  # block
                block_change_direction = blocks[table[row][col]]
                new_direction = block_change_direction[direction]
                direction = new_direction
                score += 1
            elif 6 <= table[row][col] <= 10:  # wormholes
                wormhole_pair = wormholes[table[row][col]]
                if wormhole_pair[0] == [row, col]:
                    another_one = wormhole_pair[1]
                else:
                    another_one = wormhole_pair[0]
                row = another_one[0]
                col = another_one[1]


for k in range(T):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    wormholes = defaultdict(list)
    for i in range(N):
        for j in range(N):
            if 6 <= table[i][j] <= 10:
                wormholes[table[i][j]].append([i, j])

    ans = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] != 0:
                continue
            for start_direction in range(4):
                score = get_score(table, i, j, start_direction, wormholes)
                ans = max(ans, score)
    print(f"#{k+1} {ans}")
