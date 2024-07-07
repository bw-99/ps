import sys
sys.setrecursionlimit(500*500)
input = sys.stdin.readline

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

drow, dcol = [-1, 1, 0, 0], [0, 0, -1, 1]



def dfs(row, col):
    if(SCORE_MAP[row][col] != -1):
        return SCORE_MAP[row][col]
    
    
    pos_dirs = []
    for i in range(4):
        nrow, ncol = row + drow[i], col + dcol[i]
        if(0 <= nrow < N and 0 <= ncol < N):
            if(MAP[nrow][ncol] > MAP[row][col]):
                pos_dirs.append((nrow, ncol))
                
    
    x=0
    for dir in pos_dirs:
        item = 1
        item += dfs(dir[0], dir[1])
        x = max(x, item)
        
    # 종료 조건
    if(len(pos_dirs) == 0):
        SCORE_MAP[row][col] = 1
        return SCORE_MAP[row][col]
    
    SCORE_MAP[row][col] = x
    # print(row, col, x)

    return x

sorted_arr = []
for i in range(N):
    sorted_arr.append(sorted(range(len(MAP[i])), key=lambda k: MAP[i][k],reverse=False))

# print(sorted_arr)

SCORE_MAP = [[-1 for _ in range(N)] for _ in range(N)]
x = 1
for i in range(N):
    for j in range(N):
        sorted_i, sorted_j = i, sorted_arr[i][j]
        
        if(SCORE_MAP[sorted_i][sorted_j] == -1):
            SCORE_MAP[sorted_i][sorted_j] = dfs(sorted_i, sorted_j)
            # print(sorted_i, sorted_j, SCORE_MAP)
            x = max(x, SCORE_MAP[sorted_i][sorted_j])
print(x)        
