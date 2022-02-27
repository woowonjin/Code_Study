N, M = list(map(int, input().split()))

true_person = set(list(map(int, input().split()))[1:])
parties = [set(list(map(int, input().split()))[1:]) for _ in range(M)]

lie_list = [1]*M

for _ in range(M):
    for idx, party in enumerate(parties):
        if true_person.intersection(party):
            lie_list[idx] = 0
            true_person = true_person.union(party)
print(sum(lie_list))