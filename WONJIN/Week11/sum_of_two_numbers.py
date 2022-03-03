N = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()

start = 0
end = len(nums)-1

ans = 0
while start < end:
    num1, num2 = nums[start], nums[end]
    sum_ = num1 + num2
    if sum_ == x:
        ans += 1
        start += 1
        end -= 1
    elif sum_ > x:
        end -= 1
    else:
        start += 1
print(ans)