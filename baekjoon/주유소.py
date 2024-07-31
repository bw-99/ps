import sys

input = sys.stdin.readline

N = int(input())
dist_lst = list(map(int, input().split()))
price_lst = list(map(int, input().split()))

cur_price = 0
min_price = 1e10
for i in range(N-1):
    min_price = min(min_price, price_lst[i])
    cur_price += min_price * dist_lst[i]

print(cur_price)