import sys

input = sys.stdin.readline

N, K = map(int, input().split())
GOLD, SILVER, BRONZE = 1e+7, 1, 1e-7
SCORE_LST = [0]*(N+1)
for _ in range(N):
    item = list(map(int, input().split()))
    score = GOLD*item[1] + SILVER*item[2] + BRONZE*item[3]
    SCORE_LST[item[0]] =(score)

SCORE_LST_SORTED = sorted(SCORE_LST, reverse=True)
print(SCORE_LST_SORTED.index(SCORE_LST[K]) + 1)