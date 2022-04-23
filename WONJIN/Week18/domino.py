N = int(input())

blue_table = [[False]*6 for _ in range(4)]
red_table = [[False]*4 for _ in range(6)]


def fill_red(red_table, t, x, y):
    x = 0
    if t == 1:
        while x < 5:
            if not red_table[x+1][y]:
                x += 1
            else:
                break
        red_table[x][y] = True
    elif t == 2:
        while x < 5:
            if not red_table[x+1][y] and not red_table[x+1][y+1]:
                x += 1
            else:
                break
        red_table[x][y] = True
        red_table[x][y+1] = True
    elif t == 3:
        while x+1 < 5:
            if not red_table[x+2][y]:
                x += 1
            else:
                break
        red_table[x][y] = True
        red_table[x+1][y] = True


def fill_blue(blue_table, t, x, y):
    y = 0
    if t == 1:
        while y < 5:
            if not blue_table[x][y+1]:
                y += 1
            else:
                break
        blue_table[x][y] = True
    elif t == 2:
        while y+1 < 5:
            if not blue_table[x][y+2]:
                y += 1
            else:
                break
        blue_table[x][y] = True
        blue_table[x][y+1] = True
    elif t == 3:
        while y < 5:
            if not blue_table[x][y+1] and not blue_table[x+1][y+1]:
                y += 1
            else:
                break
        blue_table[x][y] = True
        blue_table[x+1][y] = True


def red_check_and_remove(red_table):
    cnt = 0
    while True:
        is_removed = False
        for row in range(5, 1, -1):
            if all(red_table[row]):
                cnt += 1
                del red_table[row]
                red_table.insert(0, [False]*4)
                is_removed = True
                break
        if not is_removed:
            return cnt


def blue_check_and_remove(blue_table):
    cnt = 0
    while True:
        is_removed = False
        for col in range(5, 1, -1):
            col_list = [blue_table[i][col] for i in range(4)]
            if all(col_list):
                is_removed = True
                cnt += 1
                for i in range(4):
                    del blue_table[i][col]
                for i in range(4):
                    blue_table[i].insert(0, False)
                break
        if not is_removed:
            return cnt


def red_extra_remove(red_table):
    cnt = 0
    for row in range(2):
        if any(red_table[row]):
            cnt += 1
    red_table = red_table[:6-cnt]
    for _ in range(cnt):
        temp = [False]*4
        red_table.insert(0, temp)
    return red_table


def blue_extra_remove(blue_table):
    cnt = 0
    for col in range(2):
        col_list = [blue_table[i][col] for i in range(4)]
        if any(col_list):
            cnt += 1
    if cnt == 0:
        return blue_table
    for i in range(4):
        blue_table[i] = blue_table[i][:6-cnt]
        for _ in range(cnt):
            blue_table[i].insert(0, False)
    return blue_table


ans = 0
for idx in range(N):
    t, x, y = list(map(int, input().split()))
    fill_red(red_table, t, x, y)
    fill_blue(blue_table, t, x, y)
    ans += red_check_and_remove(red_table)
    ans += blue_check_and_remove(blue_table)
    red_table = red_extra_remove(red_table)
    blue_table = blue_extra_remove(blue_table)

# print(idx)
# for t in red_table:
    # print(t)
# print()
# for t in blue_table:
    # print(t)
# print("="*100)
print(ans)
cnt = 0
for row in red_table:
    cnt += sum(row)
for row in blue_table:
    cnt += sum(row)
print(cnt)
