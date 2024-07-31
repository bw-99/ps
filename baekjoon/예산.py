import sys

input = sys.stdin.readline

N = int(input())
price_lst = sorted(list(map(int, input().split())))
M = int(input())

def binary_search(min_threshold, max_threshold):
    while True:
        cur_threhold = (min_threshold + max_threshold) // 2
        tmp_sum=0
        for price in price_lst:
            if(price <= cur_threhold):
                tmp_sum+=price
            else:
                tmp_sum+=cur_threhold
        if(tmp_sum > M):
            max_threshold = cur_threhold
        elif(tmp_sum < M):
            min_threshold = cur_threhold
        else:
            break
        if(cur_threhold == (min_threshold + max_threshold) // 2):
            break
    return cur_threhold

min_threshold,max_threshold = None, None
for idx, price in enumerate(price_lst):
    tmp_sum = (N-idx)*price + sum(price_lst[:idx])
    if(tmp_sum > M):
        max_threshold = price
        break
    min_threshold = price

if(min_threshold == None):
    cur_threhold = binary_search(0, min(price_lst))    
elif(max_threshold==None):
    cur_threhold = max(price_lst)
else:
    cur_threhold = binary_search(min_threshold, max_threshold)
print(cur_threhold)