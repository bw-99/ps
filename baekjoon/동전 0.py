import sys

input = sys.stdin.readline

N, K = map(int, input().split())

NUM_LST = []
for _ in range(N):
    NUM_LST.append(int(input().strip()))

cnt = 0
for i in range(N-1, -1, -1):
    cnt += K // NUM_LST[i]
    K = K % NUM_LST[i]
print(cnt)