N = input()
nums = list(map(int, input().split()))
operators_num = list(map(int, input().split()))

max_ans = -1000000001
min_ans = 1000000001
# print(nums)
def dfs(idx, nums, operators, num_val):
    # print(f"idx : {idx}, operators : {operators}, num_val : {num_val}")
    if idx == 0:
        dfs(idx+1, nums, operators, nums[0])
    elif idx > len(nums)-1:
        global max_ans
        global min_ans
        if num_val > max_ans:
            max_ans = num_val
        if num_val < min_ans:
            min_ans = num_val
    else:
        for i, ops in enumerate(operators):
            if ops != 0:
                new_ops = operators[:]
                new_ops[i] -= 1
                if i == 0:
                    new_num_val = num_val + nums[idx]
                elif i == 1:
                    new_num_val = num_val - nums[idx]
                elif i == 2:
                    new_num_val = num_val * nums[idx]
                elif i == 3:
                    if num_val < 0 and nums[idx] > 0 or num_val > 0 and nums[idx] < 0:
                        new_num_val = -int(abs(num_val) / abs(nums[idx]))
                    else:
                        new_num_val = int(num_val / nums[idx])
                else:
                    print("error")
                dfs(idx+1, nums, new_ops, new_num_val)
dfs(0, nums, operators_num, 0)
print(max_ans)
print(min_ans)