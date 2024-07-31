import sys
import math

input = sys.stdin.readline

N = int(input())
M = int(input())
X = list(map(int, input().split()))

max_dist = X[0] - 0
for i in range(1, len(X)):
    max_dist = max(max_dist, math.ceil((X[i]- X[i-1])/2))
max_dist = max(max_dist, N-X[-1])
print(max_dist)