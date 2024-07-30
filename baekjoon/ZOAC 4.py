import sys
import math

input = sys.stdin.readline

H, W, N, M = list(map(int, input().split()))

print(int((math.ceil(H / (N+1))) * math.ceil((W / (M+1)))))