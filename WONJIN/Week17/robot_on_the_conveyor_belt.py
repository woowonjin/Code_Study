N, K = list(map(int, input().split()))

belt = list(map(int, input().split()))
robots = [False]*N


def rotate(belt):
    val = belt.pop(-1)
    belt.insert(0, val)
    robots.pop(-1)
    robots.insert(0, False)
    robots[-1] = False


def move(belt, robots):
    for i in range(N-2, -1, -1):
        if robots[i]:
            if not robots[i+1] and belt[i+1] != 0:
                robots[i+1] = True
                robots[i] = False
                belt[i+1] -= 1
    robots[-1] = False


def add(belt, robots):
    if belt[0] != 0:
        robots[0] = True
        belt[0] -= 1


def check(belt):
    cnt = 0
    for val in belt:
        if val == 0:
            cnt += 1

    return True if cnt < K else False


ans = 0
while True:
    ans += 1
    rotate(belt)
    move(belt, robots)
    add(belt, robots)
    if not check(belt):
        break
print(ans)
