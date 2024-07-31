import sys
input = sys.stdin.readline

num_lst = list(map(int, input().split()))
print(sum([item*item for item in num_lst]) % 10)