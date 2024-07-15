import sys
# import math
# print(math.pow(10, 6) * math.log2(math.pow(10, 7)))

def get_trees():
    sum_height = 0
    for item in TREE_LST:
        if(item < mid):
            continue
        sum_height +=  item - mid
    return sum_height

input = sys.stdin.readline


N, M = map(int, input().split())

TREE_LST = list(map(int, input().split()))
max_height = 0
start, end = 0, max(TREE_LST)


while True:
    if(end - start == 1):
        mid = end
        sum_height = get_trees()
        if(sum_height >= M):
            max_height = max(max_height, mid)
        
        mid = start
        sum_height = get_trees()
        if(sum_height >= M):
            max_height = max(max_height, mid)
        
        break
            
    mid = (start + end) // 2
    sum_height = get_trees()
    
    if(sum_height > M):
        max_height = max(max_height, mid)
        start = mid
    elif(sum_height == M):
        max_height = max(max_height, mid)
        start = mid
        break
    else:
        end = mid

print(max_height)