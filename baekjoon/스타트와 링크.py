import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
SELECT_LST = [False for _ in range(N)]
team = []

min_val = 200*10-2*10

def calc_score():
    teamA_lst, teamB_lst = [], []
    for i in range(N):
        if(SELECT_LST[i]):
            teamA_lst.append(i)
        else:
            teamB_lst.append(i)
    
    
    teamA_combi = combinations(teamA_lst, 2)
    teamA_score = 0
    for combi in teamA_combi:
        teamA_score += MAP[combi[0]][combi[1]] + MAP[combi[1]][combi[0]]
    
    teamB_combi = combinations(teamB_lst, 2)
    teamB_score = 0
    for combi in teamB_combi:
        teamB_score += MAP[combi[0]][combi[1]] + MAP[combi[1]][combi[0]]
    
    # print(teamA_lst, teamB_lst)
    return abs(teamA_score-teamB_score)
    
def recur(depth, prev_idx):
    global min_val
    
    if(depth == N // 2):
        score = calc_score()
        min_val = min(min_val, score)
        return
    
        
    for i in range(prev_idx, N):
        if(SELECT_LST[i]):
            continue
        
        SELECT_LST[i] = True
        recur(depth+1, i)
        SELECT_LST[i] = False
         
recur(0, 0)
print(min_val)