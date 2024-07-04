from collections import deque

N = int(input())

A = list(map(int, input().split()))
B, C = map(int, input().split())
dir_cnt = 0

A = [item - B for item in A]
dir_cnt += len(A)

for i in range(len(A)):
    if(A[i] < 0):
        continue
    tmp_dir_cnt = (A[i] // C)
    if(A[i] % C != 0):
        tmp_dir_cnt +=1
    dir_cnt+=tmp_dir_cnt

print(dir_cnt)