import sys

N = int(input())

cnt = 0
ans = -1
for num in range(666, 1000000000):
    if cnt == N:
        print(ans)
        break
    if "666" in str(num):
        cnt += 1
        ans = num


