move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def put_fish(bowls):
    min_num = min(bowls)
    for i in range(len(bowls)):
        if bowls[i] == min_num:
            bowls[i] += 1

def rotate_clockwise(block):
    return list(map(list, zip(*block[::-1])))

def move_bowls_1(bowls):
    moved_bowls = [[bowls[0]], bowls[1:]]
    while True:
        criteria = len(moved_bowls[0])
        air_bowls = []
        for i in range(len(moved_bowls)):
            if i != len(moved_bowls)-1:
                air_bowls.append(moved_bowls[i])
            else:
                air_bowls.append(moved_bowls[i][:criteria])
                new_moved_bowls = [moved_bowls[-1][criteria:]]
        rotated_bowls = rotate_clockwise(air_bowls)
        new_moved_bowls = rotated_bowls + new_moved_bowls
        if len(new_moved_bowls[0]) > len(new_moved_bowls[-1]):
            return moved_bowls
        else:
            moved_bowls = new_moved_bowls

def regulate(bowls):
    regulates_candidates = []
    for row in range(len(bowls)):
        for col in range(len(bowls[row])):
            cur_bowl_fish = bowls[row][col]
            for m_row, m_col in move:
                n_row = row + m_row
                n_col = col + m_col
                if 0 <= n_row < len(bowls):
                    if 0 <= n_col < len(bowls[n_row]):
                        if bowls[n_row][n_col] > cur_bowl_fish:
                            continue
                        quotient = (bowls[row][col]-bowls[n_row][n_col])//5
                        if quotient > 0:
                            regulates_candidates.append([[row, col], [n_row, n_col], quotient])
    for from_, to_, val in regulates_candidates:
        bowls[from_[0]][from_[1]] -= val
        bowls[to_[0]][to_[1]] += val

def stratified_bowls(bowls):
    criteria = len(bowls[0])
    stratified = []
    for col in range(criteria):
        stratified_temp = []
        for row in range(len(bowls)-1, -1, -1):
            stratified_temp.append(bowls[row][col])
        stratified += stratified_temp
    stratified += bowls[-1][criteria:]
    return stratified

def move_bowls_2(bowls):
    criteria = N // 2
    new_bowls = [bowls[:criteria][::-1], bowls[criteria:]]
    new_criteria = len(new_bowls[0]) // 2
    first_bowls = []
    second_bowls = []
    for row in new_bowls:
        first_bowls.append(row[:new_criteria])
        second_bowls.append(row[new_criteria:])
    rotated_first_1 = rotate_clockwise(first_bowls)
    rotated_first_2 = rotate_clockwise(rotated_first_1)
    return rotated_first_2 + second_bowls

N, K = list(map(int, input().split()))
bowls = list(map(int, input().split()))

cnt = 0
while True:
    if max(bowls)-min(bowls) <= K:
        break
    put_fish(bowls)
    moved_bowls = move_bowls_1(bowls)
    regulate(moved_bowls)
    new_bowls = stratified_bowls(moved_bowls)
    moved_bowls = move_bowls_2(new_bowls)
    regulate(moved_bowls)
    bowls = stratified_bowls(moved_bowls)
    cnt += 1

print(cnt)