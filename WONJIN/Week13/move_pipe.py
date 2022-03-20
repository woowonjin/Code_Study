from collections import deque

N = int(input())
table = ["".join(input().split()) for _ in range(N)]

ans = 0

# r, c, d
def dfs(p1, p2, direc):
    if p2 == [N-1, N-1]:
        global ans
        ans += 1

    if direc == "r":
        p1_n = [p1[0], p1[1]+1]
        p2_n = [p2[0], p2[1]+1]
        if 0 <= p2_n[0] < N and 0 <= p2_n[1] < N:
            if table[p2_n[0]][p2_n[1]] == "0":
                dfs(p1_n, p2_n, "r")
        p1_n = [p1[0], p1[1]+1]
        p2_n = [p2[0]+1, p2[1]+1]
        if 0 <= p2_n[0] < N and 0 <= p2_n[1] < N:
            if table[p1_n[0]][p1_n[1]+1] == "0" and table[p1_n[0]+1][p1_n[1]] == "0" and table[p1_n[0]+1][p1_n[1]+1] == "0":
                dfs(p1_n, p2_n, "d")
    elif direc == "c":
        p1_n = [p1[0]+1, p1[1]]
        p2_n = [p2[0]+1, p2[1]]
        if 0 <= p2_n[0] < N and 0 <= p2_n[1] < N:
            if table[p2_n[0]][p2_n[1]] == "0":
                dfs(p1_n, p2_n, "c")
        p1_n = [p1[0]+1, p1[1]]
        p2_n = [p2[0]+1, p2[1]+1]
        if 0 <= p2_n[0] < N and 0 <= p2_n[1] < N:
            if table[p1_n[0]][p1_n[1]+1] == "0" and table[p1_n[0]+1][p1_n[1]] == "0" and table[p1_n[0]+1][p1_n[1]+1] == "0":
                dfs(p1_n, p2_n, "d")
    elif direc == "d":
        p1_n = [p1[0]+1, p1[1]+1]
        p2_n = [p2[0], p2[1]+1]
        if 0 <= p2_n[0] < N and 0 <= p2_n[1] < N:
            if table[p2_n[0]][p2_n[1]] == "0":
                dfs(p1_n, p2_n, "r")
        p1_n = [p1[0]+1, p1[1]+1]
        p2_n = [p2[0]+1, p2[1]]
        if 0 <= p2_n[0] < N and 0 <= p2_n[1] < N:
            if table[p2_n[0]][p2_n[1]] == "0":
                dfs(p1_n, p2_n, "c")
        p1_n = [p1[0]+1, p1[1]+1]
        p2_n = [p2[0]+1, p2[1]+1]
        if 0 <= p2_n[0] < N and 0 <= p2_n[1] < N:
            if table[p1_n[0]][p1_n[1]+1] == "0" and table[p1_n[0]+1][p1_n[1]] == "0" and table[p1_n[0]+1][p1_n[1]+1] == "0":
                dfs(p1_n, p2_n, "d")

dfs([0, 0], [0, 1], "r")
print(ans)



# from collections import deque

# N = int(input())
# table = ["".join(input().split()) for _ in range(N)]

# ans = 0

# # r, c, d
# queue = deque([[[0, 0], [0, 1], "r"]])
# # dfs([0, 0], [0, 1], "r")
# while queue:
#     p1, p2, direc = queue.popleft()
#     if p2 == [N-1, N-1]:
#         ans += 1
#         continue

#     if direc == "r":
#         p1_n = [p1[0], p1[1]+1]
#         p2_n = [p2[0], p2[1]+1]
#         if 0 <= p2_n[0] < N and 0 <= p2_n[1] < N:
#             if table[p2_n[0]][p2_n[1]] == "0":
#                 queue.append([p1_n, p2_n, "r"])
#         p1_n = [p1[0], p1[1]+1]
#         p2_n = [p2[0]+1, p2[1]+1]
#         if 0 <= p2_n[0] < N and 0 <= p2_n[1] < N:
#             if table[p1_n[0]][p1_n[1]+1] == "0" and table[p1_n[0]+1][p1_n[1]] == "0" and table[p1_n[0]+1][p1_n[1]+1] == "0":
#                 queue.append([p1_n, p2_n, "d"])
#     elif direc == "c":
#         p1_n = [p1[0]+1, p1[1]]
#         p2_n = [p2[0]+1, p2[1]]
#         if 0 <= p2_n[0] < N and 0 <= p2_n[1] < N:
#             if table[p2_n[0]][p2_n[1]] == "0":
#                 queue.append([p1_n, p2_n, "c"])
#         p1_n = [p1[0]+1, p1[1]]
#         p2_n = [p2[0]+1, p2[1]+1]
#         if 0 <= p2_n[0] < N and 0 <= p2_n[1] < N:
#             if table[p1_n[0]][p1_n[1]+1] == "0" and table[p1_n[0]+1][p1_n[1]] == "0" and table[p1_n[0]+1][p1_n[1]+1] == "0":
#                 queue.append([p1_n, p2_n, "d"])
#     elif direc == "d":
#         p1_n = [p1[0]+1, p1[1]+1]
#         p2_n = [p2[0], p2[1]+1]
#         if 0 <= p2_n[0] < N and 0 <= p2_n[1] < N:
#             if table[p2_n[0]][p2_n[1]] == "0":
#                 queue.append([p1_n, p2_n, "r"])
#         p1_n = [p1[0]+1, p1[1]+1]
#         p2_n = [p2[0]+1, p2[1]]
#         if 0 <= p2_n[0] < N and 0 <= p2_n[1] < N:
#             if table[p2_n[0]][p2_n[1]] == "0":
#                 queue.append([p1_n, p2_n, "c"])
#         p1_n = [p1[0]+1, p1[1]+1]
#         p2_n = [p2[0]+1, p2[1]+1]
#         if 0 <= p2_n[0] < N and 0 <= p2_n[1] < N:
#             if table[p1_n[0]][p1_n[1]+1] == "0" and table[p1_n[0]+1][p1_n[1]] == "0" and table[p1_n[0]+1][p1_n[1]+1] == "0":
#                 queue.append([p1_n, p2_n, "d"])

# print(ans)


    


