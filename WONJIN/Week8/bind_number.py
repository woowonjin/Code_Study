N = int(input())
positives = []
negatives = []
zeros = 0
for _ in range(N):
    num = int(input())
    if num < -1000 or num > 1000:
        continue
    if num > 0:
        positives.append(num)
    elif num == 0:
        zeros += 1
    else:
        negatives.append(num)
positives.sort(reverse=True)
negatives.sort(reverse=True)
answer = 0
idx = 0
while idx < len(positives):
    if idx != len(positives)-1:
        if positives[idx] != 1 and positives[idx+1] != 1:
            answer += positives[idx]*positives[idx+1]
            idx += 2
        else:
            answer += positives[idx]
            idx += 1
    else:
        answer += positives[idx]
        idx += 1
if len(negatives) % 2 == 0:
    idx = 0
else:
    if zeros == 0:
        answer += negatives[0]
    idx = 1
while idx < len(negatives):
    answer += negatives[idx]*negatives[idx+1]
    idx += 2
print(answer)