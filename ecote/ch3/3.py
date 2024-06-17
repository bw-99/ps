

N, M = map(int, input().split(" "))
data = []

for i in range(N):
    data.append(list(map(int, input().split(" "))))
    

min_lst = [min(item) for item in data]
print(max(min_lst))