N, L = list(map(int, input().split()))

roads = [list(map(int, input().split())) for _ in range(N)]

col_roads = []
for j in range(N):
    temp = []
    for i in range(N):
        temp.append(roads[i][j])
    col_roads.append(temp)
roads += col_roads


def check(road, L):
    idx = 0
    used = [False]*len(road)
    cur_height = road[0]
    while idx < len(road):
        if road[idx] == cur_height:
            idx += 1
            continue
        if abs(cur_height-road[idx]) >= 2:
            return False
        if road[idx] > cur_height:  # 1, 1, 3 -> 앞에 놔야함
            if idx-L < 0:
                return False
            for i in range(1, L+1):
                if road[idx-i] != cur_height:
                    return False
                if used[idx-i]:
                    return False
                else:
                    used[idx-i] = True
            cur_height = road[idx]
        else:  # 2, 1, 1 -> 뒤에 놔야함
            if idx+L-1 >= len(road):
                return False
            for i in range(0, L):
                if road[idx+i] != road[idx]:
                    return False
                if used[idx+i]:
                    return False
                else:
                    used[idx+i] = True
            cur_height = road[idx]
        idx += 1
    return True


ans = 0
for road in roads:
    if check(road, L):
        ans += 1
print(ans)
