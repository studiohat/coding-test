import sys
import heapq

heap = []

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n != 0:
        heapq.heappush(heap, -n)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
