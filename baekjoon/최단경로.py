import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
K = int(input())

EDGE_LST = [[] for _ in range(V+1)]
DIST_LST = [INF] * (V+1)
for _ in range(E):
    src, tar, weight = map(int, input().split())
    EDGE_LST[src].append([weight, tar])
    
heap = [[0, K]]
DIST_LST[K]=0

while heap:
    ew, en = heapq.heappop(heap)
    if(DIST_LST[en] != ew):
        continue
    
    new_edge_lst = EDGE_LST[en]
    for (nw, nn) in new_edge_lst:
        if(DIST_LST[nn] > ew + nw):
            DIST_LST[nn] = ew + nw
            heapq.heappush(heap, [DIST_LST[nn], nn])

for item in DIST_LST[1:]:
    if(item == INF):
        print("INF")
    else:
        print(item)