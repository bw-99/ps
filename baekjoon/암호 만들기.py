import sys

input = sys.stdin.readline

L, C = list(map(int, input().split()))

STR_LST = input().split()
STR_LST = sorted(STR_LST)
VISIT_LST = [False for _ in range(C)]
candidate_answer = []

def is_valid():
    moeum_cnt, zaeum_cnt = 0, 0
    for s in candidate_answer:
        if(s in ['a', 'e', 'i', 'o', 'u']):
            moeum_cnt += 1
        else:
            zaeum_cnt += 1
    return (moeum_cnt >= 1) and (zaeum_cnt >= 2)


def recurse(cur_idx):
    if(len(candidate_answer) == L):
        if(is_valid()):
            print("".join(candidate_answer))
        return
    
    
    for i in range(cur_idx, C):
        candidate_answer.append(STR_LST[i])
        recurse(i+1)
        candidate_answer.pop()
        
recurse(0)