import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().split())
FOOD_LST = [int(input()) for _ in range(N)]

EAT_LST = [0]*(d+1)
num_diverse = 0

# * init
for j in range(k):
    food = FOOD_LST[j]
    if(EAT_LST[food] == 0):
        num_diverse+=1
    EAT_LST[food] += 1
    
if(EAT_LST[c] == 0):
    num_diverse += 1
max_diverse = num_diverse
if(EAT_LST[c] == 0):
    num_diverse -= 1
        

                
for idx in range(1, N):
    prev_food = FOOD_LST[idx-1]
    next_food = FOOD_LST[idx+k-1] if idx+k-1 < N else FOOD_LST[idx-N+k-1]
    
    # * delete
    if(EAT_LST[prev_food] != 0):
        EAT_LST[prev_food] -= 1
        if(EAT_LST[prev_food] == 0):
            num_diverse -= 1
    # * add
    if(EAT_LST[next_food] == 0):        
        num_diverse += 1
    EAT_LST[next_food] += 1
    # * coupon
    if(EAT_LST[c] == 0):
        num_diverse += 1
    # * compare
    max_diverse = max(max_diverse, num_diverse)
    if(EAT_LST[c] == 0):
        num_diverse -= 1
    
print(max_diverse)