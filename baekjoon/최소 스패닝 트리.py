# import sys
# import heapq

# input = sys.stdin.readline

# V, E = map(int, input().split())

# ADJ_MATRIX = [list(map(int, input().split())) for _ in range(E)]
# EDGE_LST = [[] for _ in range(V+1)]
# for (src, target, weight) in ADJ_MATRIX:
#     EDGE_LST[src].append([target, weight])
#     EDGE_LST[target].append([src, weight])
    
# heap = [[0, 1]]
# cost = 0
# VISITED = [False for _ in range(V+1)]
# while heap:
#     w, node = heapq.heappop(heap)
#     if(VISITED[node]):
#         continue
#     VISITED[node]=True
#     cost += w
#     new_edge_lst = EDGE_LST[node]
#     for (new_targ, new_weight) in new_edge_lst:
#         if(VISITED[new_targ]):
#             continue
#         heapq.heappush(heap, [new_weight, new_targ])
        

# print(cost)

import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
edge_lst = [[] for _ in range(V+1)]
for _ in range(E):
    start, end, cost = map(int, input().split())
    edge_lst[start].append((end, cost))
    edge_lst[end].append((start, cost))

search_lst = [[0, 1]]
visited_lst = [0]*(V+1)
cost = 0

while search_lst:
    cc, cn = heapq.heappop(search_lst)
    if(visited_lst[cn]==1):
        continue
    
    visited_lst[cn] = 1
    cost += cc
    
    for nn, nc in edge_lst[cn]:
        if(visited_lst[nn]==0):
            heapq.heappush(search_lst, [nc, nn])
            
print(cost)