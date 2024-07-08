import math
import sys

input = sys.stdin.readline
N = int(input())

sys.setrecursionlimit(10**9)

arr = [[' ' for _ in range(N)] for _ in range(N)]


def draw_outside(vertex):
    for i in range(vertex[0], vertex[1]):
        arr[i][vertex[2]] = '*'
        arr[i][vertex[3]-1] = '*'
    for i in range(vertex[2], vertex[3]):
        arr[vertex[0]][i] = '*'
        arr[vertex[1]-1][i] = '*'
        
    
# (0, N, 0, N)
def dfs(vertex):
    draw_outside(vertex)

    # 종료 조건
    if(vertex[1]-vertex[0]==3):
        return
    
    new_N = (vertex[1]-vertex[0])//3
    row_candidates = [(vertex[0], vertex[0] + new_N), (vertex[0] + new_N, vertex[0]+ new_N*2), (vertex[0] + new_N*2, vertex[0] + new_N*3)]
    col_candidates = [(vertex[2], vertex[2] + new_N), (vertex[2] + new_N, vertex[2]+ new_N*2), (vertex[2] + new_N*2, vertex[2] + new_N*3)]
    for r_idx, row in enumerate(row_candidates):
        for c_idx, col in enumerate(col_candidates):
            if(r_idx == 1 and c_idx == 1):
                continue
            # print(row+col)
            dfs(row+col)
    
    return

dfs((0, N, 0, N))


for i in range(N):
    for j in range(N):
        print(arr[i][j], end= "")
    print()
    
