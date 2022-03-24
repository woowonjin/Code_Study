from collections import Counter

r, c, k = list(map(int, input().split()))

table = [list(map(int, input().split())) for _ in range(3)]

time = 0
is_true = True
while True:
    if len(table) > r-1 and len(table[0]) > c-1:
        if table[r-1][c-1] == k:
            break

    if time >= 100:
        is_true = False
        break
    row_len = len(table)
    col_len = len(table[0])
    new_table = []
    if row_len >= col_len:
        for row in table:
            count_dict = Counter(row)
            row_arr = []
            for key, val in count_dict.items():
                if key != 0:
                    row_arr.append([key, val])
            row_arr.sort(key=lambda x: (x[1], x[0]))
            temp = []
            for arr in row_arr:
                temp += arr
            new_table.append(temp[:100])
        max_len = 3
        for row in new_table:
            max_len = max(max_len, len(row))
        for i in range(len(new_table)):
            if len(new_table[i]) < max_len:
                for _ in range(max_len-len(new_table[i])):
                    new_table[i].append(0)
    else:
        new_arr = []
        for col in range(len(table[0])):
            temp = []
            for row in range(len(table)):
                temp.append(table[row][col])
            new_arr.append(temp)
        for row in new_arr:
            count_dict = Counter(row)
            row_arr = []
            for key, val in count_dict.items():
                if key != 0:
                    row_arr.append([key, val])
            row_arr.sort(key=lambda x: (x[1], x[0]))
            temp = []
            for arr in row_arr:
                temp += arr
            new_table.append(temp[:100])
        max_len = 3
        for row in new_table:
            max_len = max(max_len, len(row))
        for i in range(len(new_table)):
            if len(new_table[i]) < max_len:
                for _ in range(max_len-len(new_table[i])):
                    new_table[i].append(0)
        new_table_transpose = []
        for j in range(len(new_table[0])):
            temp = []
            for i in range(len(new_table)):
                temp.append(new_table[i][j])
            new_table_transpose.append(temp)
        new_table = new_table_transpose

    table = new_table
    time += 1
if not is_true:
    print(-1)
else:
    print(time)
