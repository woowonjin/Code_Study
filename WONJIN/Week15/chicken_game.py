from itertools import combinations
N, M = list(map(int, input().split()))

table = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if table[i][j] == 2:
            chickens.append([i, j])
        elif table[i][j] == 1:
            houses.append([i, j])

chicken_combs = list(combinations(chickens, M))

ans = 99999
for comb in chicken_combs:
    dist = 0
    for house in houses:
        min_dist = 999999
        for chicken in comb:
            min_dist = min(min_dist, abs(
                house[0]-chicken[0])+abs(house[1]-chicken[1]))
        dist += min_dist
    ans = min(ans, dist)

print(ans)
