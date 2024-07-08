import sys
from collections import deque

input = sys.stdin.readline

NUM_TC = int(input())

for _ in range(NUM_TC):
    data = [item for item in input().strip()]
    q = deque([])
    
    for s in data:
        if(len(q) == 0):
            q.append(s)
            continue
        
        if(q[-1] == '(' and s == ')'):
            q.pop()
        else:
            q.append(s)

    if(q):
        print("NO")
    else:
        print("YES")