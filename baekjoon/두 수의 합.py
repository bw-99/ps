import sys

input = sys.stdin.readline

N = int(input())
NUM_LST = list(map(int, input().split()))
NUM_LST.sort()
X = int(input())
cnt = 0
left, right = 0, N-1

while (True):
    if(left >= right):
        break
    two_sum = NUM_LST[left] + NUM_LST[right]
    if(two_sum == X):
        left += 1
        right -= 1
        cnt += 1
    elif(two_sum < X):
        left += 1
    else:
        right -= 1

print(cnt)