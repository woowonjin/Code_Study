N, S = list(map(int, input().split()))
nums = list(map(int, input().split()))

cnt = 0
def dfs(nums, idx, val):
    global cnt
    if val == S:
        cnt += 1
    if idx >= len(nums)-1:
        return
    for i in range(idx+1, len(nums)):
        dfs(nums, i, val+nums[i])
for i in range(N):
    dfs(nums, i, nums[i])
print(cnt)