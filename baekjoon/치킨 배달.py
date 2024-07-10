import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

MAP = [list(map(int, input().split())) for _ in range(N)]

home_lst, chicken_lst = [], []
for i in range(N):
    for j in range(N):
        if(MAP[i][j] == 1):
            home_lst.append([i, j])
        elif(MAP[i][j] == 2):
            chicken_lst.append([i, j])
            
VISIT_LIST = [False for _ in range(len(chicken_lst))]
tmp_chicken_lst = []
ans = (N*2+1)*N

def chicken_distance():
    distance = 0
    for home_pose in home_lst:
        tmp_distance = N*2+1
        for chicken_pose in tmp_chicken_lst:
            dist = abs(chicken_pose[0] - home_pose[0]) + abs(chicken_pose[1] - home_pose[1])
            tmp_distance = min(dist, tmp_distance)
        distance+= tmp_distance
    return distance

def recurs(depth, cur_idx):
    global ans
    
    if(depth == M):
        ans = min(ans, chicken_distance())
        # print(ans)
        return
    
    for i in range(cur_idx, len(chicken_lst)):
        if(VISIT_LIST[i]):
            continue
        
        # print(chicken_lst[i], end= " ")
        VISIT_LIST[i]=True
        tmp_chicken_lst.append(chicken_lst[i])
        recurs(depth+1, i)
        tmp_chicken_lst.pop()
        VISIT_LIST[i]=False
        
recurs(0, 0)
print(ans)