import sys
import math

input = sys.stdin.readline
N = int(input())
MAP = [[0 for _ in range(N)] for _ in range(N)]
CNT=0

ROW_POSSIBLE = [True for _ in range(N)]
COL_POSSIBLE = [True for _ in range(N)]
POS_POSSIBLE = [True for _ in range(2*N-1)]
NEG_POSSIBLE = [True for _ in range(2*N-1)]

def get_greedy_pos(depth, r_p, c_p, p_p, n_p):
    pos_lst = []
    i = depth
    for j in range(N):
        if(r_p[i] and c_p[j] and p_p[i+j] and n_p[(N-1) - (i-j)]):
            pos_lst.append((i, j))
            
    return pos_lst

gt_lst = []

def dfs(depth, r_p, c_p, p_p, n_p):
    global CNT, gt_lst

    if(depth == N):
        CNT+=1
        return

    pos_lst = get_greedy_pos(depth, r_p, c_p, p_p, n_p)
    
    # 퀸 착수
    for pos in pos_lst:
        i,j = pos
        
        n_rp = [False if idx == i else r_p[idx] for idx in range(N)]
        n_cp = [False if idx == j else c_p[idx] for idx in range(N)]
        n_pp = [False if idx == (i+j) else p_p[idx] for idx in range(2*N-1)]
        n_np = [False if idx == (N-1) - (i-j) else n_p[idx] for idx in range(2*N-1)]
        
        dfs(depth+1, n_rp, n_cp, n_pp, n_np)

            
dfs(0, ROW_POSSIBLE, COL_POSSIBLE, POS_POSSIBLE, NEG_POSSIBLE)

print(CNT)