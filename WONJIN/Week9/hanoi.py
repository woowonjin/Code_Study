N = int(input())

cnt = 0
moves = []

def hanoi(N, start, via, to):
    global cnt
    global moves
    if N == 1:
        moves.append([start, to])
        cnt += 1
    else:
        hanoi(N-1, start, to, via)
        moves.append([start, to])
        cnt += 1
        hanoi(N-1, via, start, to)
hanoi(N, 1, 2, 3)
print(cnt)
for move in moves:
    print(move[0], move[1])