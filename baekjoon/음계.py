import sys
input = sys.stdin.readline

num_lst = list(map(int, input().split()))

ascending_lst = sorted(num_lst)
descending_lst = ascending_lst[::-1]

if(num_lst == ascending_lst):
    print("ascending")
elif(num_lst == descending_lst):
    print("descending")
else:
    print("mixed")