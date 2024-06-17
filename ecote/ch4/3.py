
def get_rot(rot):
    rot = rot - 1 if rot -1 >= 0 else 3
    return rot

N, M = map(int, input().split())
A, B, rot = map(int, input().split())

game_map = []
for i in range(N):
    game_map.append(list(map(int, input().split())))

visit_map = [[0] * N]*M
visit_map[A][B] = 1


x_action = [-1, 0, 1, 0]
y_action = [0, 1, 0, -1]

visit_cnt = 1
turn_cnt = 0
while True:
    rot = get_rot(rot)
    dx, dy = x_action[rot], y_action[rot]
    if(visit_map[A+dx][B+dy] == 0 and game_map[A+dx][B+dy] != 1):
        A=A+dx
        B=B+dy
        
        visit_cnt +=1
    else:
        turn_cnt += 1
        if(turn_cnt == 4):
            
            A=A-dx
            B=B-dy
            
            if(game_map[A][B] == 1):
                break
            visit_map[A-dx][B-dy] = 1
            turn_cnt = 0

print(visit_cnt)