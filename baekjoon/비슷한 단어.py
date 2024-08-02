# import sys
# from collections import Counter
# input = sys.stdin.readline

# N = int(input())
# word_lst = []
# for _ in range(N):
#     word_lst.append(input().rstrip())
# word_dict = {}
# for word in word_lst:
#     item = Counter(word)
#     word_dict[word]=item

# num_same = 0
# for word in word_lst[1:]:
#     print(word_dict[word], word_dict[word_lst[0]])
#     if(sorted(word_dict[word].keys()) != sorted(word_dict[word_lst[0]].keys())):
#         continue
#     sorted_key = sorted(word_dict[word_lst[0]].keys())
#     is_same = True
#     for key in sorted_key:
#         if(word_dict[word][key] != word_dict[word_lst[0]][key]):
#             is_same=False
#             continue
#     if(is_same):
#         num_same+=1
# print(num_same)