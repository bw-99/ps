import sys
from itertools import combinations

input = sys.stdin.readline

Game2Mincount = {
    "Y": 1,
    "F": 2,
    "O": 3
} 

N, game = input().strip().split()
N = int(N)

people = set([])
for _ in range(N):
    people.add(input().strip())

# print(people)
print(len(people) // Game2Mincount[game])
# print(list(combinations(people, Game2Mincount[game])))
# print(len(list(combinations(people, Game2Mincount[game]))))
