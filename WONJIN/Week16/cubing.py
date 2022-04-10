
def rotate_clockwise(table):
    return list(map(list, zip(*table[::-1])))


def rotate_counter_clockwise(table):
    return list(map(list, zip(*table)))[::-1]


def get_col_block(table, idx):
    return [table[i][idx] for i in range(3)]


def change_col_block(table, block, idx):
    for i in range(3):
        table[i][idx] = block[i]


def rotate_top_clock(top, bottom, front, back, left, right):
    top = rotate_clockwise(top)
    right_block = right[0]
    front_block = front[0]
    left_block = left[0]
    back_block = back[0]
    front[0] = right_block
    left[0] = front_block
    back[0] = left_block
    right[0] = back_block
    return top


def rotate_bottom_clock(top, bottom, front, back, left, right):
    bottom = rotate_clockwise(bottom)
    right_block = right[2]
    front_block = front[2]
    left_block = left[2]
    back_block = back[2]
    front[2] = left_block
    right[2] = front_block
    back[2] = right_block
    left[2] = back_block
    return bottom


def rotate_left_clock(top, bottom, front, back, left, right):
    # top -> front
    # front -> bottom
    # bottom -> back
    # back -> top
    left = rotate_clockwise(left)
    top_block = get_col_block(top, 0)
    front_block = get_col_block(front, 0)
    bottom_block = get_col_block(bottom, 0)
    back_block = get_col_block(back, 2)
    change_col_block(front, top_block, 0)
    change_col_block(bottom, front_block, 0)
    change_col_block(back, bottom_block[::-1], 2)
    change_col_block(top, back_block[::-1], 0)
    return left


def rotate_right_clock(top, bottom, front, back, left, right):
    right = rotate_clockwise(right)
    top_block = get_col_block(top, 2)
    front_block = get_col_block(front, 2)
    bottom_block = get_col_block(bottom, 2)
    back_block = get_col_block(back, 0)
    change_col_block(top, front_block, 2)
    change_col_block(back, top_block[::-1], 0)
    change_col_block(bottom, back_block[::-1], 2)
    change_col_block(front, bottom_block, 2)
    return right


def rotate_front_clock(top, bottom, front, back, left, right):
    front = rotate_clockwise(front)
    top_block = top[2]
    right_block = get_col_block(right, 0)
    bottom_block = bottom[0]
    left_block = get_col_block(left, 2)
    change_col_block(right, top_block, 0)
    bottom[0] = right_block[::-1]
    change_col_block(left, bottom_block, 2)
    top[2] = left_block[::-1]
    return front


def rotate_back_clock(top, bottom, front, back, left, right):
    back = rotate_clockwise(back)
    top_block = top[0]
    right_block = get_col_block(right, 2)
    bottom_block = bottom[2]
    left_block = get_col_block(left, 0)
    change_col_block(right, bottom_block[::-1], 2)
    top[0] = right_block
    change_col_block(left, top_block[::-1], 0)
    bottom[2] = left_block
    return back


def rotate_top_counter_clock(top, bottom, front, back, left, right):
    top = rotate_counter_clockwise(top)
    right_block = right[0]
    front_block = front[0]
    left_block = left[0]
    back_block = back[0]
    right[0] = front_block
    back[0] = right_block
    left[0] = back_block
    front[0] = left_block
    return top


def rotate_bottom_counter_clock(top, bottom, front, back, left, right):
    bottom = rotate_counter_clockwise(bottom)
    right_block = right[2]
    front_block = front[2]
    left_block = left[2]
    back_block = back[2]
    front[2] = right_block
    left[2] = front_block
    back[2] = left_block
    right[2] = back_block
    return bottom


def rotate_left_counter_clock(top, bottom, front, back, left, right):
    left = rotate_counter_clockwise(left)
    top_block = get_col_block(top, 0)
    front_block = get_col_block(front, 0)
    bottom_block = get_col_block(bottom, 0)
    back_block = get_col_block(back, 2)
    change_col_block(front, bottom_block, 0)
    change_col_block(top, front_block, 0)
    change_col_block(back, top_block[::-1], 2)
    change_col_block(bottom, back_block[::-1], 0)
    return left


def rotate_right_counter_clock(top, bottom, front, back, left, right):
    right = rotate_counter_clockwise(right)
    top_block = get_col_block(top, 2)
    front_block = get_col_block(front, 2)
    bottom_block = get_col_block(bottom, 2)
    back_block = get_col_block(back, 0)
    change_col_block(front, top_block, 2)
    change_col_block(bottom, front_block, 2)
    change_col_block(back, bottom_block[::-1], 0)
    change_col_block(top, back_block[::-1], 2)
    return right


def rotate_front_counter_clock(top, bottom, front, back, left, right):
    front = rotate_counter_clockwise(front)
    top_block = top[2]
    right_block = get_col_block(right, 0)
    bottom_block = bottom[0]
    left_block = get_col_block(left, 2)
    top[2] = right_block
    change_col_block(left, top_block[::-1], 2)
    bottom[0] = left_block
    change_col_block(right, bottom_block[::-1], 0)
    return front


def rotate_back_counter_clock(top, bottom, front, back, left, right):
    back = rotate_counter_clockwise(back)
    top_block = top[0]
    right_block = get_col_block(right, 2)
    bottom_block = bottom[2]
    left_block = get_col_block(left, 0)
    change_col_block(right, top_block, 2)
    bottom[2] = right_block[::-1]
    change_col_block(left, bottom_block, 0)
    top[0] = left_block[::-1]
    return back


N = int(input())

"""
Top : white
Bottom : yellow
Front : red
Back : orange
Left : green
Right : blue
"""
for _ in range(N):
    top = [["w"]*3 for _ in range(3)]
    bottom = [["y"]*3 for _ in range(3)]
    front = [["r"]*3 for _ in range(3)]
    back = [["o"]*3 for _ in range(3)]
    left = [["g"]*3 for _ in range(3)]
    right = [["b"]*3 for _ in range(3)]
    n = int(input())
    commands = input().split()
    for cmd in commands:
        surface = cmd[0]
        rotation = cmd[1]
        if surface == "U":
            if rotation == "+":
                top = rotate_top_clock(top, bottom, front, back, left, right)
            else:
                top = rotate_top_counter_clock(
                    top, bottom, front, back, left, right)
        elif surface == "D":
            if rotation == "+":
                bottom = rotate_bottom_clock(
                    top, bottom, front, back, left, right)
            else:
                bottom = rotate_bottom_counter_clock(
                    top, bottom, front, back, left, right)
        elif surface == "F":
            if rotation == "+":
                front = rotate_front_clock(
                    top, bottom, front, back, left, right)
            else:
                front = rotate_front_counter_clock(
                    top, bottom, front, back, left, right)
        elif surface == "B":
            if rotation == "+":
                back = rotate_back_clock(top, bottom, front, back, left, right)
            else:
                back = rotate_back_counter_clock(
                    top, bottom, front, back, left, right)
        elif surface == "L":
            if rotation == "+":
                left = rotate_left_clock(top, bottom, front, back, left, right)
            else:
                left = rotate_left_counter_clock(
                    top, bottom, front, back, left, right)
        elif surface == "R":
            if rotation == "+":
                right = rotate_right_clock(
                    top, bottom, front, back, left, right)
            else:
                right = rotate_right_counter_clock(
                    top, bottom, front, back, left, right)
        # print("top")
    for row in top:
        print("".join(row))
        # print()
        # print("bottom")
        # for row in bottom:
        #     print("".join(row))
        # print()
        # print("left")
        # for row in left:
        #     print("".join(row))
        # print()
        # print("right")
        # for row in right:
        #     print("".join(row))
        # print()
        # print("front")
        # for row in front:
        #     print("".join(row))
        # print()
        # print("back")
        # for row in back:
        #     print("".join(row))
        # print("="*100)
