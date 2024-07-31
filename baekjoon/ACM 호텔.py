T = int(input())

for i in range(T):
    a, b, c = map(int,input().split())
    num = c // a +1
    floor = c % a
    if c % a == 0:
        num = c//a
        floor = a
    print(f'{floor*100+num}')