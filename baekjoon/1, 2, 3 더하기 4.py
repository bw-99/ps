import sys

input = sys.stdin.readline

T = int(input())
TARGET_LST = [int(input()) for _ in range((T))]

for TARGET in TARGET_LST:
    cnt = 0
    for i in range(0, (TARGET//3) + 1):
        num_sum = TARGET
        num_sum -= i*3
        cnt += (num_sum // 2) + 1
    print(cnt)
    