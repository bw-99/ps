import sys

input = sys.stdin.readline

N, K = map(int, input().split())

NUM_LST = list(map(int, input().split()))

left, right = 0, 1
max_val = -100 * K * 2
max_val = sum(NUM_LST[:K])

num_sum = NUM_LST[0]

# * K == 1인 상황에 대한 예외 처리가 필요함
if (K==1):
    print(max(NUM_LST))
    exit()

while True:
    if(right >= N):
        break
    
    num_sum += NUM_LST[right]
    
    if(right - left + 1 == K):
        max_val = max(num_sum, max_val)
        num_sum -= NUM_LST[left]
        left += 1
        right += 1
    else:
        right += 1

print(max_val)