import sys
from collections import deque

input = sys.stdin.readline

drow = [1, 1, 1]
dcol = [-1, 0, 1]

N, M = map(int, input().split())

cost_map = [list(map(int, input().split())) for _ in range(N)]

q = deque([[(0, i), cost_map[0][i], -1] for i in range(M)])

min_cost = 100*6*6
min_cost_map = [[min_cost for _ in range(N)] for _ in range(M)]

while q:
    cur_pose, cur_cost, cur_dir = q.popleft()
    min_cost_map[new_pose[0]][new_pose[1]] 
    
    if(cur_pose[0] == N-1):
        min_cost = min(cur_cost, min_cost)
        continue
    
    for i in range(3):
        if(i == cur_dir):
            continue
        dr, dc = drow[i], dcol[i]
        new_pose = (cur_pose[0] + dr, cur_pose[1] + dc)
        if( 0<= new_pose[0] < N and 0 <= new_pose[1] < M):
            new_cost = cur_cost + cost_map[new_pose[0]][new_pose[1]]
            
            q.append([new_pose, new_cost, i])
            
print(min_cost)