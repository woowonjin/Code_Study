def check(m, n, board):
    targets = set()
    for row in range(m-1):
        for col in range(n-1):
            if board[row][col] == "0":
                continue
            if board[row][col] == board[row+1][col] == board[row][col+1] == board[row+1][col+1]:
                targets.add((row, col))
                targets.add((row+1, col))
                targets.add((row, col+1))
                targets.add((row+1, col+1))
    return targets

def find(board, row, col):
    for idx in range(row-1, -1, -1):
        if board[idx][col] != "0":
            return idx
    return -1

def remove_and_drop(m, n, board, targets):
    for row, col in targets:
        board[row][col] = "0"
    
    for col in range(n):
        row = m-1
        while row > 0:
            if board[row][col] == "0":
                idx = find(board, row, col)
                if idx == -1:
                    break
                else:
                    board[row][col] = board[idx][col]
                    board[idx][col] = "0"
            row -= 1
    return board

def solution(m, n, board):
    table = []
    for line in board:
        table.append(list(line))
    answer = 0
    while True:
        targets = check(m, n, table)
        if not targets:
            break
        answer += len(targets)
        table = remove_and_drop(m, n, table, targets)
    # print(table)
    return answer