import sys

input = sys.stdin.readline

hashmap = {}

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if(MAP[i][j] == 1):
            if(hashmap.get(i) == None):
                hashmap[i] = []
            hashmap[i].append(j) 
            
print(hashmap)

# new_map = {}
# for key, value in hashmap.items():
#     new_map[key] = []
#     items = hashmap.get(key)
#     while(items != None):
#         for item in items:
#             print(key, item)
#             new_map[key].append(item)
#             if(new_map.get(item) != None):
#                 new_map[key] += new_map.get(item)
#                 break
#             else:
#                 item = hashmap.get(item)

# print(new_map)

tmp_map = [item for item in MAP]

for key, value in new_map.items():
    for v in value:
        tmp_map[key][v]=1

print(tmp_map)