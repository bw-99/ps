from collections import deque
from copy import deepcopy

N = int(input())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))


def move_left(cur_board):
    # merge
    for i in range(len(cur_board)):
        for j in range(len(cur_board)-1):
            row_idx, col_idx = i, j
            while(col_idx < len(cur_board)-1):
                is_same = (cur_board[i][j] == cur_board[i][col_idx+1])
                is_diff = (cur_board[i][col_idx+1] != 0 and cur_board[i][j] != 0 and not is_same)
                if(is_same):
                    cur_board[i][j] += cur_board[i][col_idx+1]
                    cur_board[i][col_idx+1] = 0
                    break
                if(is_diff):
                    break
                
                col_idx+=1
    # swipe
    for i in range(len(cur_board)):
        for j in range(1, len(cur_board)):
            row_idx, col_idx = i, j
            while(col_idx > 0 and cur_board[i][col_idx-1] == 0):
                cur_board[i][col_idx-1] = cur_board[i][col_idx]
                cur_board[i][col_idx] = 0
                col_idx-=1
    return cur_board
        
def move_right(cur_board):
    # merge
    for i in range(len(cur_board)):
        for j in range(len(cur_board)-1, 0, -1):
            row_idx, col_idx = i, j
            while(col_idx > 0):
                is_same = (cur_board[i][j] == cur_board[i][col_idx-1])
                is_diff = (cur_board[i][col_idx-1] != 0 and cur_board[i][j] != 0 and not is_same)
                if(is_same):
                    cur_board[i][j] += cur_board[i][col_idx-1]
                    cur_board[i][col_idx-1] = 0
                    break
                if(is_diff):
                    break
                
                col_idx-=1
                
    # swipe
    for i in range(len(cur_board)):
        for j in range(len(cur_board)-2, -1, -1):
            row_idx, col_idx = i, j
            while(col_idx < len(cur_board)-1 and cur_board[i][col_idx+1] == 0):
                cur_board[i][col_idx+1] = cur_board[i][col_idx]
                cur_board[i][col_idx] = 0
                col_idx+=1

    return cur_board

def move_top(cur_board):
    # merge
    for j in range(len(cur_board)):
        for i in range(len(cur_board)-1):
            row_idx, col_idx = i, j
            while(row_idx < len(cur_board)-1):
                is_same = (cur_board[i][j] == cur_board[row_idx+1][j])
                is_diff = (cur_board[row_idx+1][j] != 0 and cur_board[i][j] != 0 and not is_same)
                if(is_same):
                    cur_board[i][j] += cur_board[row_idx+1][j]
                    cur_board[row_idx+1][j] = 0
                    break
                if(is_diff):
                    break
                
                
                row_idx+=1
                
    # swipe
    for j in range(len(cur_board)):
        for i in range(1, len(cur_board)):
            row_idx, col_idx = i, j
            while(row_idx > 0 and cur_board[row_idx-1][col_idx] == 0):
                cur_board[row_idx-1][col_idx] = cur_board[row_idx][col_idx]
                cur_board[row_idx][col_idx] = 0
                row_idx-=1
                
    return cur_board
        
def move_bottom(cur_board):
    # merge
    for j in range(len(cur_board)):
        for i in range(len(cur_board)-1, 0, -1):
            row_idx, col_idx = i, j
            while(row_idx > 0):
                is_same = (cur_board[i][j] == cur_board[row_idx-1][j])
                is_diff = (cur_board[i][j] != 0 and cur_board[row_idx-1][j] != 0 and not is_same)
                if(is_same):
                    cur_board[i][j] += cur_board[row_idx-1][j]
                    cur_board[row_idx-1][j] = 0
                    break
                if(is_diff):
                    break
                
                row_idx-=1
            
    # swipe
    for j in range(len(cur_board)):
        for i in range(len(cur_board)-2, -1, -1):
            row_idx, col_idx = i, j
            while(row_idx < len(cur_board)-1 and cur_board[row_idx+1][col_idx] == 0):
                cur_board[row_idx+1][col_idx] = cur_board[row_idx][col_idx]
                cur_board[row_idx][col_idx] = 0
                row_idx+=1
                
    return cur_board

if(N == 1):
    print(max(board[0]))
    exit()

q= deque([("left", [item[:] for item in board], 0), ("top", [item[:] for item in board], 0), ("right", [item[:] for item in board], 0), ("bottom", [item[:] for item in board], 0)])
max_lst = []
while(len(q)):
    
    direction, tmp_board, cnt = q.popleft()
    n = [item[:] for item in tmp_board]
    
    if(direction == "left"):
        cur_board = move_left(tmp_board)
    elif(direction == "top"):
        cur_board = move_top(tmp_board)
    elif(direction == "right"):
        cur_board = move_right(tmp_board)
    elif(direction == "bottom"):
        cur_board = move_bottom(tmp_board)
    else:
        assert False
    
    cnt += 1
    
    if(cnt >= 5):
        max_lst.append(max([max(row) for row in cur_board]))
    else:
        if(n == cur_board):
            continue
        q.append(("left", [item[:] for item in cur_board], cnt))
        q.append(("top", [item[:] for item in cur_board], cnt))
        q.append(("right", [item[:] for item in cur_board], cnt))
        q.append(("bottom", [item[:] for item in cur_board], cnt))

print(max(max_lst))