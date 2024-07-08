from collections import deque
import sys
import time

input = sys.stdin.readline
input_str = input().strip()
q = deque([])

total_div = 0
for idx, s in enumerate(input_str):
    if(len(q) == 0):
        q.appendleft((s, idx))
        continue
    tmp_s, tmp_idx = q[0]
    if(tmp_s == '(' and s == ')'):
        q.popleft()
        if(idx-tmp_idx == 1):
            # print(total_div, len(q), list(q))
            total_div+=len(q)
        else:
            total_div+=1
    else:
        q.appendleft((s, idx))
print(total_div)