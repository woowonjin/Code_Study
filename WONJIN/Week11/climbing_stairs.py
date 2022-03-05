from collections import defaultdict
N = int(input())

stairs = [int(input()) for _ in range(N)]

dp = defaultdict(int)

dp[1] = stairs[0]
if N == 1:
    print(dp[1])
    exit()
dp[2] = max(stairs[0]+stairs[1], stairs[1])
if N == 2:
    print(dp[2])
    exit()
dp[3] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])
if N == 3:
    print(dp[2])
    exit()
for i in range(4, N+1):
    dp[i] = max(dp[i-2]+stairs[i-1], dp[i-3]+ stairs[i-1] + stairs[i-2])
print(dp[N])