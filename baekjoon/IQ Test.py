from collections import deque

N = int(input())
NUM_LST = list(map(int, input().split()))
a, b = 0, 0
num_equation = N - 2

# * A
if(num_equation == -1):
    print("A")
    exit()

if(num_equation == 0):
    if(NUM_LST[0] == NUM_LST[1]):
        print(NUM_LST[1])
    else:
        print("A")
    exit()
        
    
for i in range(num_equation):
    # * solving new a, b
    if((NUM_LST[i] - NUM_LST[i+1] == 0) or (NUM_LST[i+2] - NUM_LST[i+1] == 0)):
        a_tmp = 0
        b_tmp = NUM_LST[i+1] - NUM_LST[i]*a_tmp

        if(NUM_LST[i+1] - NUM_LST[i]*a_tmp != NUM_LST[i+2] - NUM_LST[i+1]*a_tmp):
            print("B")
            exit()
    else:
        a_tmp = (NUM_LST[i+1] - NUM_LST[i+2]) / (NUM_LST[i] - NUM_LST[i+1])
        b_tmp = NUM_LST[i+1] - NUM_LST[i]*a_tmp
    
    if(i == 0):
        a, b = a_tmp, b_tmp
        
    # * compare a, b with new a, b
    B_flag1 = (a != a_tmp or b != b_tmp)
    B_flag2 = (a_tmp != int(a_tmp) or b_tmp != int(b_tmp))
    if(B_flag1 or B_flag2):
        print("B")
        exit()

print(int(NUM_LST[-1]*a + b))