from collections import deque
import sys
import time

input = sys.stdin.readline

M, N = list(map( int, input().split()))
MAP = [list(map(int, input().split())) for _ in range(M)]

start = time.time()

SCORE = [[-1 for _ in range(N)] for _ in range(M)]

drow, dcol = [-1, 1, 0, 0], [0, 0, -1, 1]

cnt = 0

def dfs(row, col):
    # 종료 조건 1
    if(row == M-1 and col == N-1):
        return 1
    
    # 종료 조건 2
    if(SCORE[row][col] != -1):
        return SCORE[row][col]
    
    x = 0
    for i in range(4):
        nrow, ncol = row + drow[i], col + dcol[i]
        
        if(0 <= nrow < M and 0 <= ncol < N and MAP[nrow][ncol] < MAP[row][col]):
            x += dfs(nrow, ncol)
            
    SCORE[row][col] = x
    return x

print(dfs(0,0))