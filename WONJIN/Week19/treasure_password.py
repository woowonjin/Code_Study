T = int(input())

base_16 = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
           "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

for t in range(T):
    N, K = list(map(int, input().split()))
    line = input()
    vals = set()
    num = N // 4
    for _ in range(N//4):
        new_line = line[-1] + line[:-1]
        for i in range(4):
            vals.add(new_line[num*i:num*i+num])
        line = new_line
    vals = list(vals)
    vals.sort(reverse=True)
    ans_16 = vals[K-1]
    ans = 0
    for idx, char in enumerate(ans_16):
        ans += pow(16, len(ans_16)-idx-1)*base_16[char]
    print(f"#{t+1} {ans}")
