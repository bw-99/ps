import sys

input = sys.stdin.readline

while True:
    x, y, z = list(map(int, input().split()))
    if(x==0 and y == 0 and z == 0):
        break
    
    if(x==y and y==z):
        print("Equilateral")
    elif(max([x, y, z]) >= sum([x, y, z]) - max([x, y, z])):
        print("Invalid")
    elif(x==y or x==z or y==z):
        print("Isosceles")
    else:
        print("Scalene")