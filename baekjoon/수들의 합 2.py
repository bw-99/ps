import sys

input = sys.stdin.readline

N, M = map(int, input().split())
NUM_LST = list(map(int, input().split()))

num_sum = NUM_LST[0]
left, right = 0, 1
cnt = 0

while True:
    if(num_sum < M):
        if(right < N):
            num_sum += NUM_LST[right]
            right += 1
        else:
            break
    elif(num_sum == M):
        cnt+=1
        num_sum -= NUM_LST[left]
        left+=1
    else:
        num_sum -= NUM_LST[left]
        left+=1
        
print(cnt)