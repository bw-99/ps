import sys
# sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input().strip())

ANSWER_LST = [False for _ in range(N)]

def dfs(n, answer):
    if(n == 1):
        return 1
    if(n == 2):
        return 2
    
    if(ANSWER_LST[n-1]):
        answer_n_1 = ANSWER_LST[n-1]
    else:
        answer_n_1 = dfs(n-1, answer) % 10007
        ANSWER_LST[n-1] = answer_n_1

    if(ANSWER_LST[n-2]):
        answer_n_2 = ANSWER_LST[n-2]
    else:
        answer_n_2 = dfs(n-2, answer) % 10007
        ANSWER_LST[n-2] = answer_n_2

    answer += answer_n_1 + answer_n_2
    return answer % 10007
    
print(dfs(N, 0))