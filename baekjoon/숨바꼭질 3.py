import sys
from collections import deque
    
input = sys.stdin.readline

N, K = map(int, input().split())

VISITED_LST = [-1] * 100_001

q = deque([(N, 0)])

    
while(q):
    cur_pos, cur_cnt = q.popleft()
    if(cur_pos == K):
        print(cur_cnt)
        break
    
    if( 0 <= cur_pos * 2 <= 100_000 and (VISITED_LST[cur_pos * 2] == -1 or VISITED_LST[cur_pos * 2] > cur_cnt)):
        q.appendleft((cur_pos* 2, cur_cnt))
        VISITED_LST[cur_pos * 2] = cur_cnt
    if( 0 <= cur_pos + 1 <= 100_000 and (VISITED_LST[cur_pos + 1] == -1 or VISITED_LST[cur_pos +1] > cur_cnt)):
        q.append((cur_pos + 1, cur_cnt+1))
        VISITED_LST[cur_pos +1] = cur_cnt+1
    if( 0 <= cur_pos - 1 <= 100_000 and (VISITED_LST[cur_pos - 1] == -1 or VISITED_LST[cur_pos -1] > cur_cnt)):
        q.append((cur_pos -1, cur_cnt+1)) 
        VISITED_LST[cur_pos -1] = cur_cnt+1