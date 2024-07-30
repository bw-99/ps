import sys

input = sys.stdin.readline

N, score, P = list(map(int, input().split()))

if(N==0):
    print(1)
else:    
    rank_lst = list(map(int, input().split()))

    for i in range(N+1):
        if(i==N):
            break
        if(rank_lst[i] < score):
            break
    if(i >= P):
        print(-1)
    else:
        for j in range(0, i+1):
            if(j==i):
                break
            if(rank_lst[i-j-1] != score):
                break
        print(i-j+1)
