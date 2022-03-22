from collections import deque


def check(snake_pos):
    for i in range(1, len(snake_pos)):
        if snake_pos[i] == snake_pos[0]:
            return False
    return True


N = int(input())
K = int(input())

apples = [list(map(int, input().split())) for _ in range(K)]
eaten = [False]*K

L = int(input())
cmd = []
for _ in range(L):
    line = input().split()
    cmd.append([int(line[0]), line[1]])


snake_pos = deque([[1, 1]])
time = 0
direction_idx = 2
directions = ["l", "t", "r", "b"]
cmd_idx = 0
while True:
    if snake_pos[0][0] < 1 or snake_pos[0][0] > N or snake_pos[0][1] < 1 or snake_pos[0][1] > N:
        break
    last_pos = snake_pos[-1][:]
    first_pos = snake_pos[0][:]
    if directions[direction_idx] == "l":
        first_pos[1] -= 1
    elif directions[direction_idx] == "t":
        first_pos[0] -= 1
    elif directions[direction_idx] == "r":
        first_pos[1] += 1
    elif directions[direction_idx] == "b":
        first_pos[0] += 1
    snake_pos.appendleft(first_pos)
    eat_apple = False
    for idx, apple_pos in enumerate(apples):
        if apple_pos == snake_pos[0] and not eaten[idx]:
            eaten[idx] = True
            eat_apple = True
            break
    if not check(snake_pos):
        time += 1
        break
    if not eat_apple:
        snake_pos.pop()
    time += 1
    if cmd_idx >= len(cmd):
        continue
    if cmd[cmd_idx][0] == time:
        if cmd[cmd_idx][1] == "L":
            direction_idx -= 1
            if direction_idx == -1:
                direction_idx = 3
        elif cmd[cmd_idx][1] == "D":
            direction_idx += 1
            if direction_idx == 4:
                direction_idx = 0
        cmd_idx += 1
print(time)
