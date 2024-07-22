import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for idx in range(T):
    NUM_LST = list(map(int, input().split()))
    NUM_LST = NUM_LST[1:]
    
    sorted_lst = deque([])
    cnt = 0
    for num in NUM_LST:
        if(len(sorted_lst) == 0):
            sorted_lst.append(num)
            continue
        
        is_max = False
        for i in range(len(sorted_lst)):
            if(sorted_lst[i] > num):
                cnt += (len(sorted_lst) - i)
                sorted_lst.insert(i, num)
                is_max = True
                break
        if(is_max):
            continue
        
        sorted_lst.append(num)
    print(idx+1, cnt)