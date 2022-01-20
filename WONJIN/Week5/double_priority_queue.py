import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    for operation in operations:
        cmd = operation.split(" ")[0]
        num = int(operation.split(" ")[1])
        if cmd == "I":
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
        elif cmd == "D" and min_heap:
            if num == 1:
                val = heapq.heappop(max_heap)
                min_heap.remove(-val)
            elif num == -1:
                val = heapq.heappop(min_heap)
                max_heap.remove(-val)
        else:
            pass
    if min_heap:
        if len(min_heap) == 1:
            val = min_heap.pop()
            return [val, val]
        else:
            min_val = heapq.heappop(min_heap)
            max_val = heapq.heappop(max_heap)
            return [-max_val, min_val]
    else:
        return [0, 0]