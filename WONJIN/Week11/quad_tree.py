N = int(input())

table = [input() for _ in range(N)]

def check(table, N, row, col):
    target = ""
    for r in range(row, row+N):
        for c in range(col, col+N):
            if r == row and c == col:
                target = table[r][c]
            else:
                if table[r][c] != target:
                    return None, False
    return target, True

def tree(table, N, row, col):
    if N==1:
        return table[row][col]
    target, res = check(table, N, row, col)
    if res:
        return f"{target}"
    else:
        lt = tree(table, N//2, row, col)
        rt = tree(table, N//2, row, col+N//2)
        lb = tree(table, N//2, row+N//2, col)
        rb = tree(table, N//2, row+N//2, col+N//2)
        return f"({lt}{rt}{lb}{rb})"
res = tree(table, N, 0, 0)
print(res)
