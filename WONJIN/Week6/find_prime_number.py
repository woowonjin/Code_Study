from itertools import permutations
import math

def is_prime(number):
    if number == 0 or number == 1:
        return False
    elif number == 2 or number == 3:
        return True
    else:
        for i in range(2, int(math.sqrt(number)+1)):
            if number % i == 0:
                return False
        return True
    

def solution(numbers):
    answer = 0
    prime_set = set()
    for i in range(1, len(numbers)+1):
        combs = list(permutations(numbers, i))
        nums = set(map(int, ["".join(comb) for comb in combs]))
        for num in nums:
            if is_prime(num):
                prime_set.add(num)
    answer = len(prime_set)
    return answer