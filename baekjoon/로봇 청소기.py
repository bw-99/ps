import sys

input = sys.stdin.readline

# 북 동 남 서
drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def rot_inv90(idx):
    return idx - 1 if idx - 1 >= 0 else 3

def backward(idx):
    return (idx+2) % 4


N, M = list(map(int, input().split()))
row, col, dir = list(map(int, input().split()))

MAP = [list(map(int, input().split())) for _ in range(N)]

def check_is_clean(row, col):
    pos_dir = []
    for i in range(4):
        nrow, ncol = row + drow[i], col + dcol[i]
        if(0<= nrow < N and 0 <= ncol < M and MAP[nrow][ncol] == 0):
            return False
    return True


cnt = 0

while True:
    # print(row, col, end =" ")
    # * 1
    if(MAP[row][col] == 0):
        MAP[row][col] = -1
        cnt+=1
    
    is_clean = check_is_clean(row, col)
    # print(is_clean)
    # * 2
    if(is_clean):
        new_dir = backward(dir)
        nrow, ncol = row + drow[new_dir], col + dcol[new_dir]
        if(0<= nrow < N and 0 <= ncol < M and MAP[nrow][ncol] != 1):
            row = nrow
            col = ncol
            continue
        else:
            print(cnt)
            break
    # * 3
    else:    
        dir = rot_inv90(dir)
        nrow, ncol = row + drow[dir], col + dcol[dir]
        if(0 <= nrow < N and 0 <= ncol < M and MAP[nrow][ncol] == 0):
            row = nrow
            col = ncol
            
            
            