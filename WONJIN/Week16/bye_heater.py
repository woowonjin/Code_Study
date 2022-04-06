from collections import defaultdict, deque
from copy import deepcopy

R, C, K = list(map(int, input().split()))
table = [list(map(int, input().split())) for _ in range(R)]

W = int(input())
wall_info = [list(map(int, input().split())) for _ in range(W)]
walls = []
for x, y, t in wall_info:
    x -= 1
    y -= 1
    temp = []
    temp.append([x, y])
    if t == 0:
        temp.append([x-1, y])
    else:
        temp.append([x, y+1])
    temp2 = [temp[1], temp[0]]
    walls.append(temp)
    walls.append(temp2)


heaters = defaultdict(list)
temp_inspect = []

for i in range(R):
    for j in range(C):
        if table[i][j] == 0:
            continue
        elif table[i][j] == 5:
            temp_inspect.append([i, j])
        else:
            heaters[table[i][j]].append([i, j])

right_to = [(-1, 1), (0, 1), (1, 1)]
right_restrictions = [[[(0, 0), (-1, 0)], [(-1, 0), (-1, 1)]],
                      [[(0, 0), (0, 1)]], [[(0, 0), (1, 0)], [(1, 0), (1, 1)]]]

left_to = [(-1, -1), (0, -1), (1, -1)]
left_restrictions = [
    [[(0, 0), (-1, 0)], [(-1, 0), (-1, -1)]], [[(0, 0), (0, -1)]], [[(0, 0), (1, 0)], [(1, 0), (1, -1)]]]

top_to = [(-1, -1), (-1, 0), (-1, 1)]
top_restrictions = [
    [[(0, 0), (0, -1)], [(0, -1), (-1, -1)]], [[(0, 0), (-1, 0)]], [[(0, 0), (0, 1)], [(0, 1), (-1, 1)]]]

bottom_to = [(1, -1), (1, 0), (1, 1)]
bottom_restrictions = [
    [[(0, 0), (0, -1)], [(0, -1), (1, -1)]], [[(0, 0), (1, 0)]], [[(0, 0), (0, 1)], [(0, 1), (1, 1)]]]


def check(row, col, conditions):
    for condition in conditions:
        res_1 = [row+condition[0][0], col+condition[0][1]]
        res_2 = [row+condition[1][0], col+condition[1][1]]
        if [res_1, res_2] in walls:
            return False
    return True


def get_heat(room):
    for key, loc in heaters.items():
        if key == 1:
            to = right_to
            restrict = right_restrictions
        elif key == 2:
            to = left_to
            restrict = left_restrictions
        elif key == 3:
            to = top_to
            restrict = top_restrictions
        elif key == 4:
            to = bottom_to
            restrict = bottom_restrictions
        for row, col in loc:
            if key == 1:
                start_row = row
                start_col = col+1
            elif key == 2:
                start_row = row
                start_col = col-1
            elif key == 3:
                start_row = row-1
                start_col = col
            elif key == 4:
                start_row = row+1
                start_col = col
            if start_row >= R or start_row < 0 or start_col < 0 or start_col >= C:
                continue
            if [[row, col], [start_row, start_col]] in walls:
                continue
            visited = [[False]*C for _ in range(R)]
            temp_room = [[0]*C for _ in range(R)]
            queue = deque()
            queue.append([start_row, start_col, 5])
            visited[start_row][start_col] = True
            temp_room[start_row][start_col] = 5
            while queue:
                r, c, h = queue.popleft()
                if h == 1:
                    continue
                for idx, [m_row, m_col] in enumerate(to):
                    n_row = r + m_row
                    n_col = c + m_col
                    if 0 <= n_row < R and 0 <= n_col < C:
                        if visited[n_row][n_col]:
                            continue
                        conditions = restrict[idx]
                        if check(r, c, conditions):
                            visited[n_row][n_col] = True
                            temp_room[n_row][n_col] = h-1
                            queue.append([n_row, n_col, h-1])
            for i in range(R):
                for j in range(C):
                    room[i][j] += temp_room[i][j]


def manipulate(room):
    temp_room = deepcopy(room)
    move = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    for row in range(R):
        for col in range(C):
            if temp_room[row][col] < 4:
                continue
            for m_row, m_col in move:
                n_row = row + m_row
                n_col = col + m_col
                if 0 <= n_row < R and 0 <= n_col < C:
                    if [[row, col], [n_row, n_col]] in walls:
                        continue
                    if temp_room[row][col] > temp_room[n_row][n_col]:
                        m_temper = (temp_room[row][col] -
                                    temp_room[n_row][n_col]) // 4
                        room[row][col] -= m_temper
                        room[n_row][n_col] += m_temper


def side(room):
    for col in range(C):
        if room[0][col] != 0:
            room[0][col] -= 1
        if room[R-1][col] != 0:
            room[R-1][col] -= 1
    for row in range(R):
        if row == 0 or row == R-1:
            continue
        if room[row][0] != 0:
            room[row][0] -= 1
        if room[row][C-1] != 0:
            room[row][C-1] -= 1


def check_temperatures(room):
    for row, col in temp_inspect:
        if room[row][col] < K:
            return False
    return True


def heat(room, get_room):
    for i in range(R):
        for j in range(C):
            room[i][j] += get_room[i][j]


get_room = [[0]*C for _ in range(R)]
room = [[0]*C for _ in range(R)]
get_heat(get_room)
chocolates = 0
while True:
    heat(room, get_room)
    manipulate(room)
    side(room)
    chocolates += 1
    if check_temperatures(room):
        break
    if chocolates > 100:
        break
if chocolates > 100:
    print(101)
else:
    print(chocolates)
