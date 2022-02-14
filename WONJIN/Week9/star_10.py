def paint(row, col, N, table):
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                pass
            else:
                if N == 3:
                    table[i+row][j+col] = True
                else:
                    paint(row+i*N//3, col+j*N//3, N//3, table)

N = int(input())
table = [[False for _ in range(N)] for _ in range(N)]
paint(0, 0, N, table)
# for t in table:
#     print(t)
for i in range(N):
    for j in range(N):
        if table[i][j]:
            print("*", end="")
        else:
            print(" ", end="")
    if i != N-1:
        print()