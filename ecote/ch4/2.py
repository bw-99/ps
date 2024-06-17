col, row = input()

col = ord(col) - ord('a')
row = int(row)-1

action_lst = [
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1),
]

cnt = 0
for action in action_lst:
    x, y = row + action[0], col + action[1]
    if(x < 0 or y < 0 or x >7 or y > 7):
        continue
    cnt+=1
print(cnt)