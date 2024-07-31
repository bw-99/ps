import sys

input = sys.stdin.readline

A, B, C = [int(input()) for _ in range(3)]
print(A+B-C)
print(int(str(A)+str(B)) -C)