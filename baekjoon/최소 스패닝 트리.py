import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())

ADJ_MATRIX = [list(map(int, input().split())) for _ in range(E)]
EDGE_LST = [[] for _ in range(V+1)]
for (src, target, weight) in ADJ_MATRIX:
    EDGE_LST[src].append([target, weight])
    EDGE_LST[target].append([src, weight])
    
heap = [[0, 1]]
cost = 0
VISITED = [False for _ in range(V+1)]
while heap:
    w, node = heapq.heappop(heap)
    if(VISITED[node]):
        continue
    VISITED[node]=True
    cost += w
    new_edge_lst = EDGE_LST[node]
    for (new_targ, new_weight) in new_edge_lst:
        if(VISITED[new_targ]):
            continue
        heapq.heappush(heap, [new_weight, new_targ])
        

print(cost)