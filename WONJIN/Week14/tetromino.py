N, M = list(map(int, input().split()))

table = [list(map(int, input().split())) for _ in range(N)]

ans = -1

shape_1 = [[[0, 0], [0, 1], [0, 2], [0, 3]], [[0, 0], [1, 0], [2, 0], [3, 0]]]
shape_2 = [[[0, 0], [0, 1], [1, 0], [1, 1]]]
shape_3 = [[[0, 0], [1, 0], [2, 0], [2, 1]], [[0, 0], [1, 0], [2, 0], [
    2, -1]], [[0, 0], [0, 1], [0, 2], [1, 2]], [[0, 0], [0, 1], [0, 2], [-1, 2]], [[0, 0], [0, 1], [1, 1], [2, 1]], [[0, 0], [0, 1], [1, 0], [2, 0]], [[0, 0], [0, 1], [0, 2], [1, 0]], [[0, 0], [-1, 0], [0, 1], [0, 2]]]
shape_4 = [[[0, 0], [1, 0], [1, 1], [2, 1]], [[0, 0], [1, 0], [1, -1], [2, -1]],
           [[0, 0], [1, 0], [0, 1], [1, -1]], [[0, 0], [0, 1], [1, 1], [1, 2]]]
shape_5 = [[[0, 0], [0, 1], [0, 2], [1, 1]], [[0, 0], [0, 1], [0, 2], [
    -1, 1]], [[0, 0], [1, 0], [2, 0], [1, 1]], [[0, 0], [1, 0], [2, 0], [1, -1]]]
shapes_all = shape_1 + shape_2 + shape_3 + shape_4 + shape_5


def check(row, col, shapes):
    is_true = True
    num = 0
    for shape in shapes:
        n_row = row + shape[0]
        n_col = col + shape[1]
        if 0 <= n_row < N and 0 <= n_col < M:
            num += table[n_row][n_col]
        else:
            is_true = False
            break
    return is_true, num


for shapes in shapes_all:
    for row in range(N):
        for col in range(M):
            checked, num = check(row, col, shapes)
            if checked:
                # print(row, col, num, ans, shapes)
                # for idx, shape in enumerate(shapes):
                #     print(
                #         f"{idx}, row : {row + shape[0]}, col : {col + shape[1]}")
                ans = max(ans, num)
print(ans)
