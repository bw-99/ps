import sys

input = sys.stdin.readline

N,M = map(int, input().split())

VISITED_LST = [False for _  in range(N+1)]

answer = []
def recurse():
    
    if(len(answer) == M):
        print(" ".join(map(str, answer)))
        return
    
    for i in range(1, N+1):
        if(VISITED_LST[i]):
            continue
        
        answer.append(i)
        VISITED_LST[i] = True
        
        recurse()
        
        answer.pop()
        VISITED_LST[i] = False
        
recurse()