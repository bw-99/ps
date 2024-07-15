import sys

input = sys.stdin.readline

N = int(input())
T_lst, P_lst = [], []
for _ in range(N):
    t, p = map(int, input().split())
    T_lst.append(t)
    P_lst.append(p)
    
COST_LST = [-1]*N


def recurse(date):
    # print(COST_LST, date)
    
    if(not(0 <= date < N)):
        return 0
    
    fmax_rev = 0
    for d in range(date, N):
        # print(date, d)
        max_rev = 0
        if(COST_LST[d] != -1):
            max_rev = COST_LST[d]
        elif((0 <= d + T_lst[d] < N+1)):
            tmp_rev = P_lst[d]
            tmp_date = d + T_lst[d]
            tmp_rev += recurse(tmp_date)
            max_rev = max(max_rev, tmp_rev)
            COST_LST[d] = max_rev
        else:
            max_rev=0
            COST_LST[d] = max_rev
        fmax_rev = max(fmax_rev, max_rev)
        
    COST_LST[date] = max(COST_LST[date], fmax_rev)
    return COST_LST[date]

recurse(0)
print(max(COST_LST))