import sys

input = sys.stdin.readline

angle_lst = []
sum_angle = 0
is_eq = True
for _ in range(3):
    angle = int(input())
    angle_lst.append(angle)
    sum_angle += angle
    is_eq &= (angle == 60)

if(sum_angle != 180):
    print("Error")
    exit()

if(is_eq):
    print("Equilateral")
    exit()

if((angle_lst[0] == angle_lst[1]) or (angle_lst[1] == angle_lst[2]) or (angle_lst[0] == angle_lst[2])):
    print("Isosceles")
    exit()

print("Scalene")
