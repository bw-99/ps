import sys
input = sys.stdin.readline

N, X = map(int, input().split())
num_visitor_lst = list(map(int, input().split()))

num_sum = sum(num_visitor_lst[0:X])
max_sum = num_sum
max_count = 1

for i in range(N-X):
    num_sum -= num_visitor_lst[i]
    num_sum += num_visitor_lst[i+X]
    if(num_sum > max_sum):
        max_sum = num_sum
        max_count=1
    elif(num_sum == max_sum):
        max_count+=1
    else:
        continue

if(max_sum == 0):
    print("SAD")
else:
    print(max_sum)
    print(max_count)