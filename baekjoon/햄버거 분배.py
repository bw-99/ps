import sys
input = sys.stdin.readline

N, K = map(int, input().split())
str_lst = [item for item in input().rstrip()]
num_eat = 0
is_eated_lst = [0]*(N)
for idx, item in enumerate(str_lst):
    if(item == "H"):
        continue
    
    # find minimum hamburger index
    min_idx = max(0, idx-K)
    max_idx = min(idx+K, N-1)
    for i in range(min_idx, max_idx+1):
        if(str_lst[i] == "H" and is_eated_lst[i] == 0):
            is_eated_lst[i] = 1
            num_eat+=1
            break
print(num_eat)
# print("".join(str_lst))
# print("".join(map(str, is_eated_lst)), sum(is_eated_lst))