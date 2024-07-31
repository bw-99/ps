import sys

input = sys.stdin.readline

N, D = map(int, input().split())

SHORT_LST = []
for _ in range(N):
    short = tuple(map(int, input().split()))
    if(short[1] - short[0] > short[2] and short[1] <= D):
        SHORT_LST.append(short)

def recurse(dist, start_pos):
    if(start_pos == D):
        return dist
    
    pos_short_lst = []
    for short in SHORT_LST:
        if(short[0] >= start_pos and short[1] <= D):
            pos_short_lst.append(short)
    if(len(pos_short_lst) == 0):
        return dist + D - start_pos
    
    min_dist_result = D
    for pos_short in pos_short_lst:
        tmp_start_pos = pos_short[1]
        tmp_dist = pos_short[2] + (pos_short[0] - start_pos) + dist
        # print("from ", start_pos, "visit ", pos_short)
        dist_result = recurse(tmp_dist, tmp_start_pos)
        min_dist_result = min(min_dist_result, dist_result)
    return min_dist_result
        
        
dist = recurse(0, 0)
print(dist)