import sys
from collections import Counter
input = sys.stdin.readline

N, M = map(int, input().split())

# 1) filtering
word_lst = []
for _ in range(N):
    word = input().rstrip()
    if(len(word) >= M):
        word_lst.append(word)

# 2) calc frequency
freq = Counter(word_lst)
set_word_lst = list(set(word_lst))
word_len = [len(word) for word in set_word_lst]
word2dictorder = dict(zip(sorted(set_word_lst), [len(set_word_lst)-i for i in range(len(set_word_lst))]))
sorted_idx = sorted([i for i in range(len(set_word_lst))], key=lambda idx: (freq[set_word_lst[idx]], word_len[idx], word2dictorder[set_word_lst[idx]]), reverse=True)

for idx in sorted_idx:
    print(set_word_lst[idx])