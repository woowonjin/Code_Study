def solution(numbers):
    numbers = list(map(str, numbers))
    changed_nums = []
    for idx, num in enumerate(numbers):
        changed_nums.append([idx, num*(6//len(num))])
    changed_nums.sort(key=lambda x : x[1], reverse=True)
    answer = ""
    for idx, _ in changed_nums:
        answer += numbers[idx]
    return str(int(answer))