def solution(N, number):
    dp = {}
    answer = -1
    for n_cnt in range(1, 9):
        op_set = set()
        max_num = int(str(N)*n_cnt)
        op_set.add(max_num)
        for j in range(1, n_cnt):
            for op1 in dp[j]:
                for op2 in dp[n_cnt-j]:
                    op_set.add(op1+op2)
                    op_set.add(op1-op2)
                    op_set.add(op1*op2)
                    if op2 != 0:
                        op_set.add(op1//op2)
        dp[n_cnt] = op_set
        if number in op_set:
            answer = n_cnt
            break