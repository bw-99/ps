import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

res = []

def recurs(cur_idx): 
    if(len(res) == M):
        print(" ".join(map(str, res)))
        return
    
    for i in range(cur_idx+1, N+1):
        res.append(i)
        recurs(i)
        res.pop()
        
recurs(0)