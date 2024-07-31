import sys
from collections import Counter
input = sys.stdin.readline

NUM_TC = int(input())

for _ in range(NUM_TC):
    N = int(input())
    RANK_LST = list(map(int, input().split()))
    c = Counter(RANK_LST)
    
    # * filter under 6
    accepted_teams = []
    for num, team in zip(c.values(), c.keys()):
        if(num < 6):
            continue
        accepted_teams.append(team)
    
    # * rank
    new_rank_lst = [item for item in RANK_LST if item in accepted_teams]
    new_score_dict = dict.fromkeys(accepted_teams, 0)
    is_four_dict = dict.fromkeys(accepted_teams, 0)
    for idx, team in enumerate(new_rank_lst):
        if(is_four_dict[team] < 4):
            is_four_dict[team] += 1
            new_score_dict[team] += idx+1
    
    
    # * compare
    team_lst = sorted(new_score_dict.keys(), key=lambda idx:new_score_dict[idx])
    
    if(len(team_lst)==1):
        print(team_lst[0])
    elif(new_score_dict[team_lst[0]] < new_score_dict[team_lst[1]]):
        print(team_lst[0])
    else:
        min_score = new_score_dict[team_lst[0]]
        same_score_team_lst = []
        for team in team_lst:
            if(new_score_dict[team] == min_score):
                same_score_team_lst.append(team)
        
        five_rank_dict = dict.fromkeys(same_score_team_lst, 0)
        winner = same_score_team_lst[0]
        for team in new_rank_lst:
            if(team not in same_score_team_lst):
                continue
            five_rank_dict[team]+=1
            if(five_rank_dict[team] == 5):
                winner = team
                break
        print(winner)
        
        
