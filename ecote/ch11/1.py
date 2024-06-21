

N = int(input())

scare_lst = list(map(int, input().split()))
scare_lst = sorted(scare_lst, reverse=False)
print(scare_lst)
group_cnt = 0
i=0

while True:
    if(i < len(scare_lst)):
        min_cnt = scare_lst[i]
        i+=min_cnt
        if(i < len(scare_lst)):
            break
        new_min_cnt = scare_lst[i]
        if(new_min_cnt > min_cnt):
            break
        group_cnt+=1
    else:
        break
        
print(group_cnt)