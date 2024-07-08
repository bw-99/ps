import sys
from itertools import combinations

input = sys.stdin.readline

num_lst = []
for _ in range(9):
    num_lst.append(int(input().strip()))
    
q = combinations(num_lst, 7)
for item in q:
    if(sum(item) == 100):
        for num in item:
            print(num)
        break