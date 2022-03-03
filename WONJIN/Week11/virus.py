from collections import deque, defaultdict
N = int(input())
nums = int(input())

computers = [0 for _ in range(N+1)]

edges = defaultdict(list)
for _ in range(nums):
    edge = list(map(int, input().split()))
    edges[edge[0]].append(edge[1])
    edges[edge[1]].append(edge[0])

queue = deque([1])
while queue:
    node = queue.popleft()
    computers[node] = 1
    for n in edges[node]:
        if computers[n] == 0:
            queue.append(n)
print(sum(computers)-1)
