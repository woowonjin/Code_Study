def solution(cacheSize, cities):
    time = 0
    cache = []
    cnt = 0
    answer = 0
    if cacheSize == 0:
        return 5*len(cities)
    for city in cities:
        city = city.lower()
        is_in = False
        for loc, t in cache:
            if loc == city:
                is_in = True
                break
        if cnt < cacheSize and not is_in:
            cache.append([city, time])
            cnt += 1
            answer += 5
        else:
            is_changed = False
            min_time = 99999
            min_idx = -1
            for idx, [loc, t] in enumerate(cache):
                if loc == city:
                    cache[idx][1] = time
                    is_changed = True
                    break
                if t < min_time:
                    min_time = t
                    min_idx = idx
            if not is_changed:
                del cache[min_idx]
                cache.append([city, time])
                answer += 5
            else:
                answer += 1
        # print(city, cache, answer)
        time += 1
    return answer

# print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
# print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
# print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
# print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
# print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
# print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Seoul", "Seoul", "Seoul"]))