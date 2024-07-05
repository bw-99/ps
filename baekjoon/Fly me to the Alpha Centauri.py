from collections import deque
import math
import sys
input = sys.stdin.readline

NUM_TC = int(input())

for _ in range(NUM_TC):
    cnt = 0
    cur_pose, tar_pose = list(map(int, input().split()))
    
    distance = tar_pose - cur_pose
    
    n1 = int(math.sqrt(distance))
    n2 = int(((-1 + math.sqrt(1 + 4*distance))/2))
    n3 = int((-2 + math.sqrt(4+4*distance))/2)
    
    d_lst = [n1*n1, n2*(n2+1), n3*(n3+2)]
    max_d = max(d_lst)
    max_n = 0
    distance -= max_d
    
    if(d_lst[0] == max_d):
        cnt += n1 * 2 -1
        max_n = n1
    elif(d_lst[1] == max_d):
        cnt += n2  * 2
        max_n = n2
    else:
        cnt += n3 * 2 +1
        max_n = n3
        
    if(distance == 0):
        pass
    elif(distance <= max_n):
        cnt += 1
        distance = 0
        
    print(cnt)
