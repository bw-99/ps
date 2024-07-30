import sys

input = sys.stdin.readline

N = int(input())
BALL_LST = [item for item in input().strip()]

if(N == 1):
    print(0)
    exit()


num_blue, num_red = [], []
cur_color = BALL_LST[0]
if(cur_color == "R"):
    num_red = [0]
else:
    num_blue = [0]

sum_num_blue, sum_num_red = 0, 0

for i in range(0, N):
    if(cur_color == BALL_LST[i]):
        if(cur_color == "R"):
            num_red[len(num_red)-1] += 1
            sum_num_red += 1
        else:
            num_blue[len(num_blue)-1] += 1
            sum_num_blue += 1
    else:
        if(BALL_LST[i] == "R"):
            num_red.append(1)
            sum_num_red += 1
            cur_color="R"
        else:
            num_blue.append(1)
            sum_num_blue += 1
            cur_color="B"
            
if(sum_num_blue == 0 or sum_num_red == 0):
    print(0)
    exit()


# * 1) blue-red
if(BALL_LST[-1] == "R" and BALL_LST[0] == "B"):
    min_cnt1 = min(sum_num_red-num_red[-1], sum_num_blue-num_blue[0])
elif(BALL_LST[-1] == "R" and BALL_LST[0] == "R"):
    min_cnt1 = min(sum_num_red-num_red[-1], sum_num_blue)
elif(BALL_LST[-1] == "B" and BALL_LST[0] == "B"):
    min_cnt1 = min(sum_num_red, sum_num_blue-num_blue[0])
elif(BALL_LST[-1] == "B" and BALL_LST[0] == "R"):
    min_cnt1 = min(sum_num_red, sum_num_blue)
    
# * 2) red-blue
if(BALL_LST[0] == "R" and BALL_LST[-1] == "B"):
    min_cnt2 = min(sum_num_red-num_red[0], sum_num_blue-num_blue[-1])
elif(BALL_LST[0] == "R" and BALL_LST[-1] == "R"):
    min_cnt2 = min(sum_num_red-num_red[0], sum_num_blue)
elif(BALL_LST[0] == "B" and BALL_LST[-1] == "B"):
    min_cnt2 = min(sum_num_red, sum_num_blue-num_blue[-1])
elif(BALL_LST[0] == "B" and BALL_LST[-1] == "R"):
    min_cnt2 = min(sum_num_red, sum_num_blue)
    
print(min(min_cnt1, min_cnt2))