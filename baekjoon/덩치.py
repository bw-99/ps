import sys

input = sys.stdin.readline

N = int(input())

VOL_LST = [tuple(map(int, input().split())) for _ in range(N)]

RANK_LST = [-1]*N

for i in range(N):
    value = VOL_LST[i]
    cnt = 1
    for j in range(N):
        if(j==i):
            continue
            
        if(VOL_LST[j][0] > value[0] and VOL_LST[j][1] > value[1]):
            cnt+=1
    print(cnt, end=" ")