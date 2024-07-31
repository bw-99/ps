import sys
from collections import deque
import heapq
INF = float("inf")
input = sys.stdin.readline

N, E = map(int, input().split())
EDGE_LST = [[] for _ in range(N+1)]


for _ in range(E):
    start, end, cost = map(int, input().split())
    EDGE_LST[start].append([end, cost])
    EDGE_LST[end].append([start, cost])
    
v1, v2  = map(int, input().split())

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
        
cost_1 = dijkstra(1)
cost_v1 = dijkstra(v1)
cost_v2 = dijkstra(v2)

# 1) 1 -> v1 -> v2 -> N
cost_first = cost_1[v1] + cost_v1[v2] + cost_v2[N]
# 2) 1 -> v2 -> v1 -> N
cost_second = cost_1[v2] + cost_v2[v1] + cost_v1[N]
min_cost = min(cost_first, cost_second)
if(min_cost == INF):
    print(-1)
else:
    print(min_cost)