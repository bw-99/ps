import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

hashmap = {}

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

# * BFS
# for i in range(N):
#     hashmap[i] = []
#     for j in range(N):
#         if(MAP[i][j] == 1):
#             hashmap[i].append(j) 

# printmap = [item for item in MAP]

# for key, value in hashmap.items():
#     if(len(value) == 0):
#         continue
    
#     q = deque([item for item in value])
#     while(q):
#         v = q.popleft()
#         printmap[key][v] = 1

#         if(hashmap.get(v)):
#             for v_tmp in hashmap.get(v):
#                 if(printmap[key][v_tmp] == 0):
#                     q.append(v_tmp)

# for i in range(N):
#     for j in range(N):
#         print(printmap[i][j], end = " ")
#     print()

# * F.W
VISMAP = [item for item in MAP]

for target_idx in range(N):
    
    for row in range(N):
        if(row == target_idx):
            continue
        for col in range(N):
            if(col == target_idx):
                continue
            if(VISMAP[row][target_idx] == 0 or VISMAP[target_idx][col] == 0):
                continue
            VISMAP[row][col]=1
            # VISMAP[row][col] = min(VISMAP[row][col], VISMAP[row][target_idx] + VISMAP[target_idx][col])
for i in range(N):
    for j in range(N):
        print(VISMAP[i][j], end = " ")
    print()
    