import sys

input = sys.stdin.readline

N, S = map(int, input().split())
NUM_LST = list(map(int, input().split()))

sum_cnt = 0
num_sum = 0

answer = N*2

for i in range(N):
    sum_cnt += 1
    num_sum += NUM_LST[i]
    
    if(num_sum < S):
        continue
    
    prev_gap = 0
    while(num_sum >= S):
        prev_gap += 1
        num_sum -= NUM_LST[i-sum_cnt +prev_gap]
    
    num_sum += NUM_LST[i-sum_cnt +prev_gap]
    prev_gap -= 1
    sum_cnt -= prev_gap
    
    answer = min(answer, sum_cnt)

if(answer == N*2):
    print(0)
else:
    print(answer)
