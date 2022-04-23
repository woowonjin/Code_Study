from ast import Break
import copy
from collections import defaultdict
origin_path = [i*2 for i in range(1, 21)]
path_25 = [30, 35, 40]
path_10 = [i*2 for i in range(1, 6)] + [13, 16, 19, 25] + path_25
path_20 = [i*2 for i in range(1, 11)] + [22, 24, 25] + path_25
path_30 = [i*2 for i in range(1, 16)] + [28, 27, 26, 25] + path_25

horses_info = {i: ["origin", -1, False]
               for i in range(4)}  # path_name, idx, finished

share_path = {"origin": 19, "10": 8, "20": 12, "30": 18}
path_length = {"origin": 20, "10": 12, "20": 16, "30": 22}

move = list(map(int, input().split()))
ans = -1
history = defaultdict(list)

cnt = 0


def dfs(horses_info_, move_idx, score, history_):
    # if history_[0] == [4, 1] and history_[2] == [3] and history_[1] == [4, 4, 4, 4, 2, 2] and move_idx == 9:
    #     print(history_)
    #     print(move_idx)
    #     print(horses_info_)
    #     print()
    if move_idx >= len(move):
        global ans
        global cnt
        cnt += 1
        # if score > ans:
        # for key, val in history_.items():
        #     if val == [4, 4, 4, 4, 2, 2]:
        #         print(score)
        #         print(horses_info_)
        #         for key, val in history_.items():
        #             print(f"{key} : {val}")
        #         print()
        # if history_[0] == [4, 1, 4] and history_[3] == [4, 4, 4, 4, 2, 2]:
        #     print(score)
        #     print(horses_info_)
        #     for key, val in history_.items():
        #         print(f"{key} : {val}")
        #     print()
        ans = max(ans, score)
        return

    for id, [path_name, horse_idx, finished] in horses_info_.items():
        if finished:
            continue
        next_horse_idx = horse_idx + move[move_idx]
        if path_name == "origin":
            path = origin_path
        elif path_name == "10":
            path = path_10
        elif path_name == "20":
            path = path_20
        elif path_name == "30":
            path = path_30

        if next_horse_idx >= len(path):
            horses_info = copy.deepcopy(horses_info_)
            horses_info[id] = [path_name, -100, True]
            history = copy.deepcopy(history_)
            history[id].append(move[move_idx])
            dfs(horses_info, move_idx+1, score, history)
        else:
            new_score = score + path[next_horse_idx]
            new_path = path_name
            if path[next_horse_idx] == 10 and path_name == "origin":
                new_path = "10"
            elif path[next_horse_idx] == 20 and path_name == "origin":
                new_path = "20"
            elif path[next_horse_idx] == 30 and path_name == "origin":
                new_path = "30"
            is_in = False
            for key, val in horses_info_.items():
                if key == id or val[2]:
                    continue
                if val[0] == new_path and val[1] == next_horse_idx:
                    is_in = True
                    break
                elif next_horse_idx >= share_path[new_path]:
                    if next_horse_idx == path_length[new_path]-1:
                        if val[1] == path_length[val[0]]-1:
                            is_in = True
                            break
                    elif val[1] - share_path[val[0]] == next_horse_idx-share_path[new_path]:
                        if val[0] == "origin" or new_path == "origin":
                            continue
                        # if history_[0] == [4, 1] and history_[2] == [3] and history_[1] == [4, 4, 4, 4, 2, 2] and move_idx == 9 and id == 0:
                        #     print(f"{key}: {val}")
                        is_in = True
                        break
            if not is_in:
                horses_info = copy.deepcopy(horses_info_)
                horses_info[id] = [new_path, next_horse_idx, finished]
                history = copy.deepcopy(history_)
                history[id].append(move[move_idx])
                dfs(horses_info, move_idx+1, new_score, history)


if move[0] == 5:
    horses_info[0] = ["10", move[0]-1, False]
    history[0].append(move[0])
else:
    horses_info[0] = ["origin", move[0]-1, False]
    history[0].append(move[0])
dfs(horses_info, 1, origin_path[move[0]-1], history)
# dfs(horses_info, 0, 0, history)
print(ans)
