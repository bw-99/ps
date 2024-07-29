import sys
from collections import deque
input = sys.stdin.readline

def print_acceptable(word):
    print(f"<{''.join(word)}> is acceptable.")
    
def print_unacceptable(word):
    print(f"<{''.join(word)}> is not acceptable.")
while True:
    passwd = input().strip()
    if(passwd=="end"):
        break
    
    aeiou_lst = ["a", "e", "i", "o", "u"]
    
    passwd = [p for p in passwd]
    
    if(len(passwd)==1):
        if(passwd[0] in aeiou_lst):
            print_acceptable(passwd)
        else:
            print_unacceptable(passwd)
        continue

    if(len(passwd) == 2):
        two_sequence=False
        if((passwd[0]==passwd[1])):
            if((passwd[0]=="e" or passwd[0]=="o")):
                two_sequence=True
            else:
                two_sequence=False
                print_unacceptable(passwd)
                continue
        
        include_aeiou = False
        for item in passwd:
            if(item in aeiou_lst):
                include_aeiou=True
                continue
        if(not include_aeiou):
            print_unacceptable(passwd)
        else:
            print_acceptable(passwd)
        continue
            
    # length >= 3
    include_aeiou = False

    for item in aeiou_lst:
        if(item in passwd):
            include_aeiou=True
            continue            
    
    if(not include_aeiou):
        print_unacceptable(passwd)
        continue
    
    three_sequence = False
    
    seq_aeiou = [1 if item in aeiou_lst else 0 for item in passwd]
    for idx in range(len(passwd)-2):
        if(seq_aeiou[idx] == 1 and seq_aeiou[idx+1] == 1 and seq_aeiou[idx+2] == 1):
            three_sequence=True
            continue
        
        if(seq_aeiou[idx]==0 and seq_aeiou[idx+1]==0 and seq_aeiou[idx+2]==0):
            three_sequence=True
            continue
    
    if(three_sequence):
        print_unacceptable(passwd)
        continue
    
    two_sequence=False
    for idx in range(len(passwd)-1):
        if((passwd[idx] == passwd[idx+1]) and not (passwd[idx] == "e" or passwd[idx] == "o")):
            two_sequence=True
            continue
    
    if(two_sequence):
        print_unacceptable(passwd)
        continue
        
    print_acceptable(passwd)