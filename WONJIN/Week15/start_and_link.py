N = int(input())

table = [list(map(int, input().split())) for _ in range(N)]

ans = 99999999


def dfs(start, link, start_score, link_score, idx):
    if idx == N:
        if len(start) == len(link):
            global ans
            ans = min(ans, abs(start_score - link_score))
        return
    if len(start) < N // 2:
        if not start:
            dfs(start+[idx], link, start_score, link_score, idx+1)
        else:
            new_start_score = start_score
            for i in start:
                new_start_score += table[i][idx] + table[idx][i]
            dfs(start+[idx], link, new_start_score, link_score, idx+1)
    if len(link) < N // 2:
        if not link:
            dfs(start, link+[idx], start_score, link_score, idx+1)
        else:
            new_link_score = link_score
            for i in link:
                new_link_score += table[i][idx] + table[idx][i]
            dfs(start, link+[idx], start_score, new_link_score, idx+1)


dfs([], [], 0, 0, 0)
print(ans)
