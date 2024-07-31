import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())
EDGE_LST = [[] for _ in range(M+1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    EDGE_LST[start].append([end, cost])
    
K, D = map(int, input().split())

search_lst = [[0, K]]
COST_LST = [float("inf")] * (N+1)
COST_LST[K] = 0
visited_lst = [0] * (N+1)

while search_lst:
    cc, cn = heapq.heappop(search_lst)
    if(cc > COST_LST[cn]):
        continue
    visited_lst[cn] = 1
    for nn, nc in EDGE_LST[cn]:
        if(COST_LST[nn] > cc + nc):
            COST_LST[nn] = cc + nc
            if(visited_lst[nn] == 0):
                heapq.heappush(search_lst, [COST_LST[nn], nn])
                
print(COST_LST[D])