N = int(input())

lines = []
for _ in range(N):
    line = list(map(int, input().split()))
    lines.append(line)

lines.sort(key=lambda x : x[0])

dp = [1]*N

for i in range(1, N):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(N-max(dp))