from collections import defaultdict
N = int(input())

table = [list(map(int, input().split())) for _ in range(N)]

dp = defaultdict(int)

for idx, [t, p] in enumerate(table):
    idx += 1
    dp[idx] = max(dp[idx-1], dp[idx])
    dp[idx+t-1] = max(dp[idx-1] + p, dp[idx+t-1])


print(dp[N])
