import sys

input = sys.stdin.readline

hashmap = {}
num_str = input().strip()

cur_num = num_str[0]

hashmap['0'] = 0
hashmap['1'] = 0
hashmap[cur_num] += 1
for num in num_str[1:]:
    if(cur_num == num):
        continue

    cur_num = num
    hashmap[cur_num] += 1

print(min(hashmap.values()))    