from itertools import combinations

line = input()
while line != "0":
    nums = list(map(int, line.split()))[1:]
    combs = list(combinations(nums, 6))
    for comb in combs:
        for i, num in enumerate(comb):
            if i == 5:
                print(num)
            else:
                print(num, end=" ")
    line = input()
    if line != "0":
        print()