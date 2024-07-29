import sys

input = sys.stdin.readline

N = int(input().strip())

COOKIE_MAP = [[item for item in input().strip()] for _ in range(N)]

heart = None

# find heart
for i in range(N):
    for j in range(N):
        if(COOKIE_MAP[i][j]=='*'):
            heart = [i+1, j]
            break
    if(heart):
        break
    
# left arm
left_arm_length = 1
while(heart[1]-left_arm_length-1 >= 0 and COOKIE_MAP[heart[0]][heart[1]-left_arm_length-1] == '*'):
    left_arm_length+=1

# right arm
right_arm_length = 1
while(heart[1]+right_arm_length+1 < N and COOKIE_MAP[heart[0]][heart[1]+right_arm_length+1] == '*'):
    right_arm_length+=1
    
# hurry
hurry_length = 1
while(heart[0]+hurry_length+1 < N and COOKIE_MAP[heart[0]+hurry_length+1][heart[1]] == '*'):
    hurry_length+=1

leg_middle_point = [heart[0]+hurry_length, heart[1]]
left_leg_start_point = [leg_middle_point[0]+1, leg_middle_point[1]-1]
right_leg_start_point = [leg_middle_point[0]+1, leg_middle_point[1]+1]

# make same as arms, hurry
left_leg_start_point[0]=left_leg_start_point[0]-1
right_leg_start_point[0]=right_leg_start_point[0]-1

# left leg
left_leg_length = 1
while(left_leg_start_point[0]+left_leg_length+1 < N and COOKIE_MAP[left_leg_start_point[0]+left_leg_length+1][left_leg_start_point[1]] == '*'):
    left_leg_length+=1
    
# right leg
right_leg_length = 1
while(right_leg_start_point[0]+right_leg_length+1 < N and COOKIE_MAP[right_leg_start_point[0]+right_leg_length+1][right_leg_start_point[1]] == '*'):
    right_leg_length+=1


print(heart[0]+1, heart[1]+1)
print(left_arm_length, right_arm_length, hurry_length, left_leg_length, right_leg_length)