import math
import itertools

input = __import__('sys').stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]

    all_possible_idx = itertools.combinations(range(N), N//2)
    answer = 1e9
    for idx_tuple in all_possible_idx:
        idx_pos = [False for _ in range(N)]
        for idx in idx_tuple:
            idx_pos[idx] = True

        vector = [0,0]
        for i in range(N):
            if idx_pos[i]:
                vector[0] += points[i][0]
                vector[1] += points[i][1]
            else:
                vector[0] -= points[i][0]
                vector[1] -= points[i][1]

        diff = math.sqrt((vector[0])**2 + (vector[1])**2)
        answer = min(answer, diff)
    print(answer)