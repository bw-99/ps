import sys

input = sys.stdin.readline

N= int(input())

hashmap = {}

for _ in range(N):
    x, y = list(map(int, input().split()))
    if(hashmap.get(y) == None):
        hashmap[y] = []
    hashmap[y].append(x)

sorted_keys = sorted(hashmap.keys())
for key in sorted_keys:
    for v in sorted(hashmap[key]):
        print(v, key)