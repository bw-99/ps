import sys
import math

input = sys.stdin.readline



def man_switching(number):
    global SWITCH_LST
    i=1
    while(number*i-1 < len(SWITCH_LST)):
        SWITCH_LST[number*i-1] = int(not SWITCH_LST[number*i-1])
        i+=1

def girl_switching(number):
    global SWITCH_LST
    num = number-1
    SWITCH_LST[num] = int(not SWITCH_LST[num])
    size = 1
    while(True):
        if((0 <= num-size < len(SWITCH_LST)) and (0 <= num+size < len(SWITCH_LST)) and SWITCH_LST[num-size] == SWITCH_LST[num+size]):
            SWITCH_LST[num-size] = int(not SWITCH_LST[num-size])
            SWITCH_LST[num+size] = int(not SWITCH_LST[num+size])
            size+=1
        else:
            break

gender2action = {
    1: man_switching,
    2: girl_switching
}

N = int(input())
SWITCH_LST = list(map(int, input().split()))
num_iter = int(input())
for _ in range(num_iter):
    gender, index = map(int, input().split())
    gender2action[gender](index)

# print(SWITCH_LST)
num_row = math.ceil(len(SWITCH_LST) / 20)
for row in range(num_row):
    start_idx = row*20
    end_idx = start_idx+20 if start_idx+20 <= len(SWITCH_LST) else len(SWITCH_LST)
    print(" ".join(map(str, SWITCH_LST[start_idx:end_idx])))