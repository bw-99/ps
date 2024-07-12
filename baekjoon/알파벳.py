import sys

input = sys.stdin.readline

R, C = map(int, input().split())

MAP = [[item for item in input().strip()] for _ in range(R)]

drow, dcol = [-1, 1, 0, 0], [0, 0, -1, 1]
hashmap = {}
row, col = 0,0
max_depth = 0

def recurs(depth):
    global row, col, max_depth
    
    hashmap[MAP[row][col]] = 1
    print(hashmap)
    go_cnt = 0
    for i in range(4):
        nrow, ncol = row + drow[i], col + dcol[i]
        if(0 <= nrow < R and 0 <= ncol < C and hashmap.get(MAP[nrow][ncol]) == None):
            go_cnt += 1
            row, col = nrow, ncol
            recurs(depth+1)
            row -= drow[i]
            col -= dcol[i]
            hashmap.pop(MAP[nrow][ncol])
            
    if(go_cnt == 0):
        max_depth = max(depth, max_depth)
        return
    
recurs(1)
print(max_depth)
