N = int(input())

nums = list(map(int, input().split()))

nums.sort()
left = 0
right = N-1
acid = nums[0] + nums[-1]
ans = [nums[0], nums[-1]]
while left < right:
    res_1 = nums[left]
    res_2 = nums[right]
    if abs(res_1+res_2) < abs(acid):
        acid = res_1+res_2
        ans = [res_1, res_2]

    if res_1 + res_2 < 0:
        left += 1
    elif res_1 + res_2 == 0:
        ans = [res_1, res_2]
        break
    else:
        right -= 1
ans.sort()
print(ans[0], ans[1])