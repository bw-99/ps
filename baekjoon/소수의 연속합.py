import sys

input = sys.stdin.readline

N = int(input())

if(N == 1):
    print(0)
    exit()

PR_BOOL_LST = [True for _ in range(N+1)]
PR_BOOL_LST[0], PR_BOOL_LST[1]=False, False
PR_LST = []
for i in range(2, N+1):
    if(PR_BOOL_LST[i]):
        PR_LST.append(i)
        number = i + i
        while(number < N+1):
            PR_BOOL_LST[number] = False
            number += i

# PR_LST = [i for i in range(0, N+1) if PR_BOOL_LST[i]]
left, right = 0, 0
# print(PR_LST)
num_sum = PR_LST[0]
cnt = 0
while True:
    # print(num_sum, left, right)
    if(num_sum < N):
        right += 1
        if(right == len(PR_LST)):
            break
        num_sum += PR_LST[right]
    elif(num_sum == N):
        cnt += 1
        num_sum -= PR_LST[left]
        left += 1
    else:
        num_sum -= PR_LST[left]
        left += 1
    
    if(left == len(PR_LST) or right == len(PR_LST)):
        break
    

print(cnt)