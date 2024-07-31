# import sys
# import heapq
# input = sys.stdin.readline
# INF = sys.maxsize

# V, E = map(int, input().split())
# K = int(input())

# EDGE_LST = [[] for _ in range(V+1)]
# DIST_LST = [INF] * (V+1)
# for _ in range(E):
#     src, tar, weight = map(int, input().split())
#     EDGE_LST[src].append([weight, tar])
    
# heap = [[0, K]]
# DIST_LST[K]=0

# while heap:
#     ew, en = heapq.heappop(heap)
#     if(DIST_LST[en] != ew):
#         continue
    
#     new_edge_lst = EDGE_LST[en]
#     for (nw, nn) in new_edge_lst:
#         if(DIST_LST[nn] > ew + nw):
#             DIST_LST[nn] = ew + nw
#             heapq.heappush(heap, [DIST_LST[nn], nn])

# for item in DIST_LST[1:]:
#     if(item == INF):
#         print("INF")
#     else:
#         print(item)

import sys
from collections import deque
import heapq
INF = sys.maxsize
input = sys.stdin.readline

N, E = map(int, input().split())
EDGE_LST = [[] for _ in range(N+1)]
K = int(input())


for _ in range(E):
    start, end, cost = map(int, input().split())
    EDGE_LST[start].append([end, cost])


def dijkstra(node):
    heap = [[0, node]]
    VISITED_LST = [0] * (N+1)
    COST_LST = [INF] * (N+1)
    COST_LST[node] = 0
    
    while heap:
        cost, targ_node = heapq.heappop(heap)
        if(COST_LST[targ_node] < cost):
            continue
        VISITED_LST[targ_node] = 1
        
        for new_node, new_cost in EDGE_LST[targ_node]:
            if(COST_LST[new_node] > new_cost + cost):
                COST_LST[new_node] = new_cost + cost
                
                if(VISITED_LST[new_node] == 1):
                    continue
                heapq.heappush(heap, [COST_LST[new_node], new_node])
    return COST_LST
        
DIST_LST = dijkstra(K)
for item in DIST_LST[1:]:
    if(item == INF):
        print("INF")
    else:
        print(item)