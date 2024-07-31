import sys
input = sys.stdin.readline

num_lst = input().rstrip()

n=0
idx=0
while True:
    n+=1
    
    for item in str(n):
        if(item==num_lst[idx]):
            idx+=1
        
        if(idx == len(num_lst)):
            print(n)
            exit()