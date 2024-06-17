


if __name__=="__main__":
    N, M, K = [eval(item) for item in input("").split(" ")]
    lst = ([eval(item) for item in input("").split(" ")])
    lst = sorted(lst, reverse=True)
    
    cnt_dict = {(k, lst[k]): 0 for k in range(0, len(lst))}
    cnt = 0
    i=0
    while(i < M):
        dict_keys = list(cnt_dict.keys())
        
        sum_flag = True
        for idx in range(len(dict_keys)):
            key = dict_keys[idx]
            if(sum_flag and cnt_dict[key] < K):
                cnt_dict[key] += 1
                cnt+=key[1]
                sum_flag = False
            else:
                cnt_dict[key] = 0
        i+=1
        
    print(cnt)
    