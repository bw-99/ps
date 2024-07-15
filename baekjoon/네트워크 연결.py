import heapq
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

EDGE_LST = [[] for _ in range(N+1)]

for _ in range(M):
    src, tar, weight = map(int, input().split())
    if(src == tar):
        continue
    EDGE_LST[src].append([tar, weight])
    EDGE_LST[tar].append([src, weight])

heap = [[0, 1]]
VISITED_LST = [False]*(N+1)
cost = 0
while heap:
    weight, tar = heapq.heappop(heap)
    if(VISITED_LST[tar]):
        continue
    cost += weight
    VISITED_LST[tar] = True
    
    new_edge_lst = EDGE_LST[tar]
    for (new_tar, new_weight) in new_edge_lst:
        if(VISITED_LST[new_tar]):
            continue
        heapq.heappush(heap, [new_weight, new_tar])
        
print(cost)