from collections import defaultdict

n, k = list(map(int, input().split()))

coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort()

cnt_dict = defaultdict(int)
cnt_dict[0] = 1
for coin in coins:
    for i in range(1, k+1):
        if coin == 1:
            cnt_dict[i] += 1
        else:
            if i < coin:
                continue
            else:
                cnt_dict[i] += cnt_dict[i-coin]
print(cnt_dict[k])