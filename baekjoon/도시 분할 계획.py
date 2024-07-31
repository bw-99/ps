import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

EDGE_LST = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, c = map(int, input().split())
    EDGE_LST[s].append((e, c))
    EDGE_LST[e].append((s, c))

search_lst = [[0, 1]]
visit_lst = [0]*(N+1)
cost = 0
max_cost = 0
while search_lst:
    cc, cn = heapq.heappop(search_lst)
    if(visit_lst[cn] == 1):
        continue
    cost+=cc
    max_cost = max(max_cost, cc)
    visit_lst[cn] = 1
    
    for nn, nc in EDGE_LST[cn]:
        if(visit_lst[nn] == 0):
            heapq.heappush(search_lst, [nc, nn])

print(cost - max_cost)