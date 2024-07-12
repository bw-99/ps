import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
NUM_LST = list(map(int, input().split()))

M = int(input())
TARGET_LST = list(map(int, input().split()))

NUM_LST.sort()


for target in TARGET_LST:
    is_in = 0
    if(N == 1):
        print(int(target == NUM_LST[0]))
        continue
    start_idx, end_idx = 0, N-1
    # print(target)
    while(start_idx < end_idx):
        
        if(end_idx - start_idx == 1):
            if(NUM_LST[start_idx] == target or NUM_LST[end_idx] == target):
                is_in=1
            break

        mid_idx = (start_idx + end_idx) // 2
        # print(start_idx, end_idx, mid_idx)

        if(NUM_LST[mid_idx] > target):
            end_idx = mid_idx
        elif(NUM_LST[mid_idx] == target):
            is_in = 1
            break
        else:
            start_idx = mid_idx
            

        
    print(is_in)