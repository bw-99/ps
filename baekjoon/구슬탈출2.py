from collections import deque
N, M = map(int, input().split())
map_info = [list(input().rstrip()) for _ in range(N)]
visited = []

dx_lst = [1, -1, 0, 0]
dy_lst = [0, 0, -1, 1]
cnt = 0

def get_pos():
    rx, ry, bx, by = 0,0,0,0
    for i in range(N):
        if("R" in map_info[i]):
            rx, ry = i, map_info[i].index("R")
        if("B" in map_info[i]):
            bx, by = i, map_info[i].index('B')
    return rx, ry, bx, by

def move(x, y, dx, dy):
    move_cnt = 0
    while(map_info[x+dx][y+dy] != "#" and map_info[x][y] != "O"):
        x+=dx
        y+=dy
        move_cnt+=1
    return x, y, move_cnt


rx, ry, bx, by = get_pos()
q= deque()
q.append((rx, ry, bx, by, 1))
visited.append((rx, ry, bx, by))

while(q):
    rx, ry, bx, by, result = q.popleft()
    if(result > 10 ):
        continue
    
    for i in range(4):
        nrx, nry, nrr = move(rx, ry, dx_lst[i], dy_lst[i])
        nbx, nby, nbr = move(bx, by, dx_lst[i], dy_lst[i])
        
        if(nrx == nbx and nry == nby):
            if(nrr > nbr):
                nrx -= dx_lst[i]
                nry -= dy_lst[i]
            else:
                nbx -= dx_lst[i]
                nby -= dy_lst[i]          
        
        if(map_info[nbx][nby] == "O"):
            continue
        
        if(map_info[nrx][nry] == "O"):
            print(result)
            exit()
                
        if (nrx, nry, nbx, nby) not in visited:
            visited.append((nrx, nry, nbx, nby))
            q.append((nrx, nry, nbx, nby, result+1))

print(-1)
    
