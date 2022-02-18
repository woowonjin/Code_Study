from itertools import combinations
L, C = list(map(int, input().split()))
chars = input().split()

consonants = []
vowels = []

for char in chars:
    if char in "aeiou":
        vowels.append(char)
    else:
        consonants.append(char)

all_combs = set()
for num_vowel in range(1, L-1):
    vowel_combs = list(combinations(vowels, num_vowel))
    conso_combs = list(combinations(consonants, L-num_vowel))
    for v_comb in vowel_combs:
        for c_comb in conso_combs:
            comb = list(v_comb + c_comb)
            comb.sort()
            all_combs.add("".join(comb))
all_combs = list(all_combs)
all_combs.sort()
for comb in all_combs:
    print(comb)
