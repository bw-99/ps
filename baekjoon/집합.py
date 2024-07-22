import sys

input = sys.stdin.readline

M = int(input())

S = set([])

for _ in range(M):
    ops = input().strip().split()
    
    if(len(ops) == 1 and ops[0] == "all"):
        S = set([i+1 for i in range(20)])
        continue
    elif(len(ops) == 1 and ops[0] == "empty"):
        S = set([])
        continue
        
    operation, num = ops
    num = int(num)
    
    if(operation == "add"):
        S.add(num)
    elif(operation == "remove"):
        S.discard(num)
    elif(operation == "check"):
        if(num in S):
            print(1)
        else:
            print(0)
    elif(operation == "toggle"):
        if(num in S):
            S.discard(num)
        else:
            S.add(num)
    