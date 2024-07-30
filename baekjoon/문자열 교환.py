import sys
from collections import Counter
input = sys.stdin.readline
input_str = input().strip()
c = Counter(input_str)
num_a = c['a']

STR_LST = [item for item in input_str]

min_b = len(STR_LST)
for i in range(len(STR_LST)):
    if(i+num_a >= len(STR_LST)):
        tmp_lst = STR_LST[i:len(STR_LST)]+STR_LST[0:i+num_a-len(STR_LST)]
    else:
        tmp_lst = STR_LST[i:i+num_a]
    num_b = Counter(tmp_lst)['b']
    min_b = min(min_b, num_b)
print(min_b)