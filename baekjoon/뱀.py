N = int(input())
K = int(input())
# print(N,K)

map_data = [[0]*N for _ in range(N)]
snake_data = [[0]*N for _ in range(N)]
for i in range(K):
    x, y = map(int, input().split())
    map_data[x-1][y-1] = 1
# print(map_data)

L = int(input())
orientation_dict = {}
for i in range(L):
    time, dir = input().split()
    time = int(time)
    orientation_dict[time]=dir
# print(orientation_dict)

dir2dir = {
    ("D", "D") : "B",
    ("B", "D") : "L",
    ("L", "D") : "T",
    ("T", "D") : "D",    
    
    ("D", "L") : "T",
    ("B", "L") : "D",
    ("L", "L") : "B",
    ("T", "L") : "L",    
}

dir2action = {
    "D": (0, 1),
    "B": (1, 0),
    "T": (-1, 0),
    "L": (0, -1),
}


is_finish = False
cur_dir = "D"
x, y = 0, 0
cnt = 0
snake_lst = []
while(not is_finish):
    
    dx, dy = dir2action[cur_dir]
    nx, ny = x+dx, y+dy
    snake_lst.insert(0, (x, y))
    # print(nx, ny)
    
    is_inside = (nx >= 0 and nx < N and ny >= 0 and ny < N)
    is_nocollide = ((nx, ny) not in snake_lst)
    if(not is_inside or not is_nocollide):
        is_finish=True
        cnt+=1
        break
    
    if(map_data[nx][ny]==1):
        # print("eat apple")
        map_data[nx][ny] = 0
        
    else:
        snake_lst.pop()
        
    
        
    cnt += 1
    x, y=nx, ny
    # print(cnt, " ", snake_lst)
    
    if(orientation_dict.get(cnt)):
        # print("change_dir : ", cur_dir, " -> ", end="")
        change_dir = orientation_dict.get(cnt)
        cur_dir = dir2dir[(cur_dir, change_dir)]
        # print(cur_dir)
        
print(cnt)