def solution(m, n, puddles):
    answer = 0
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1] = 1
    for row in range(1, n+1):
        for col in range(1, m+1):
            if row == 1 and col == 1:
                continue
            if [col, row] in puddles:
                dp[row][col] = 0
            else:
                dp[row][col] = (dp[row-1][col] + dp[row][col-1]) % 1000000007
    
    answer = dp[n][m]
    return answer%1000000007