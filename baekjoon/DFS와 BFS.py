import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

EDGE_LST = [[] for _ in range((N+1))]
for _ in range(M):
    start, end = map(int, input().split())
    EDGE_LST[start].append(end)
    EDGE_LST[end].append(start)
    
# DFS
VISITED_LST = [0]*(N+1)
q = deque([V])
while q:
    start_node = q.pop()
    if(VISITED_LST[start_node] == 1):
        continue
    VISITED_LST[start_node] = 1
    print(start_node, end=" ")
    
    # find candidates
    candidates = sorted(EDGE_LST[start_node], reverse=True)
    if(len(candidates) == 0):
        continue
    for candidate in candidates:
        if(VISITED_LST[candidate] == 0):
            q.append(candidate)
print()
# BFS
VISITED_LST = [0]*(N+1)
q = deque([V])
while q:
    start_node = q.popleft()
    if(VISITED_LST[start_node] == 1):
        continue
    VISITED_LST[start_node] = 1
    print(start_node, end=" ")
    
    # find candidates
    candidates = sorted(EDGE_LST[start_node])
    if(len(candidates) == 0):
        continue
    for candidate in candidates:
        if(VISITED_LST[candidate] == 0):
            q.append(candidate)
            
