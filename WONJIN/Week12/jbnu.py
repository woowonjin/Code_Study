from collections import defaultdict
import bisect

N, M, K = list(map(int, input().split()))

db = defaultdict(lambda: -1)

for _ in range(N):
    k, v = list(map(int, input().split()))
    db[k] = v

def find_key(keys, key, db, K):
    idx = bisect.bisect_left(keys, key)
    if idx == 0:
        if abs(keys[0]-key) <= K:
            return keys[0]
        else:
            return -1
    elif idx == len(keys):
        if abs(keys[-1]-key) <= K:
            return keys[-1]
        else:
            return -1
    else:
        calc1 = abs(keys[idx]-key)
        calc2 = abs(keys[idx-1]-key)
        if calc1 > K and calc2 > K:
            return -1
        if calc1 == calc2:
            return -2
        elif calc1 < calc2:
            return keys[idx]
        else:
            return keys[idx-1]


keys = list(db.keys())
keys.sort()
for _ in range(M):
    inst = list(map(int, input().split()))
    if inst[0] == 1:
        key, val = inst[1], inst[2]
        db[key] = val
        bisect.insort(keys, key)
    elif inst[0] == 2:
        key, val = inst[1], inst[2]
        if db[key] != -1:
            db[key] = val
        else:
            idx = find_key(keys, key, db, K)
            if idx >= 0:
                db[idx] = val
    elif inst[0] == 3:
        key = inst[1]
        idx = find_key(keys, key, db, K)
        if idx >= 0:
            print(db[idx])
        elif idx == -1:
            print(-1)
        elif idx == -2:
            print("?")

