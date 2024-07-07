import sys

input = sys.stdin.readline

N = int(input())
num_lst = list(map(int, input().split()))
M = int(input())
test=list(map(int, input().split()))

hashmap = {}

for num in num_lst:
    if(hashmap.get(num)):
        hashmap[num] += 1
    else:
        hashmap[num] = 1
        
for t in test:
    item = hashmap.get(t)
    if(item):
        print(item, end = " ")
    else:
        print(0, end = " ")
        
