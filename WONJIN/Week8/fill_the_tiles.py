N = int(input())
if N % 2 == 1:
    print(0)
else:
    dp = {}
    dp_1 = {}
    for i in range(0, N+1, 2):
        if i == 0:
            dp[i] = 1
            dp_1[i] = 0
        elif i == 2:
            dp[i] = 3
            dp_1[i] = 0
        else:
            dp_1[i] = dp_1[i-2] + dp[i-4]
            dp[i] = dp[i-2]*3 + dp_1[i]*2
    print(dp[N])