N = int(input())
times = list(map(int, input().split()))

times.sort()
sum_ = 0
ans = 0
for time in times:
    sum_ += time
    ans += sum_
print(ans)