# import sys
# input = sys.stdin.readline

# N = int(input())

# class Node():
#     def __init__(self, name, left, right):
#         self.name = name
#         self.left = left
#         self.right = right
        
# tree={}
# for _ in range(N):
#     name, left, right = map(str, input().split())
#     tree[name] = Node(name, left, right)

# def preorder(node):
#     print(node.name, end = '')
#     if node.left != '.':
#         preorder(tree[node.left])
#     if node.right != '.':
#         preorder(tree[node.right])
        
# def inorder(node):
#     if(node.left != "."):
#         inorder(tree[node.left])
#     print(node.name, end="")
#     if(node.right != "."):
#         inorder(tree[node.right])

# def postorder(node):
#     if(node.left != "."):
#         postorder(tree[node.left])
#     if(node.right != "."):
#         postorder(tree[node.right])
#     print(node.name, end="")

# preorder(tree["A"])
# print()
# inorder(tree["A"])
# print()
# postorder(tree["A"])

import sys
input = sys.stdin.readline

class Node:
    def __init__(self, left, root, right):
        self.left = left
        self.root = root
        self.right = right

tree= {}
N= int(input())
for _ in range(N):
    root, left, right = map(str, input().split())
    tree[root] = Node(left, root, right)

# 1) preorder
def preorder(root:Node):
    print(root.root, end="")
    if(root.left != "."):
        preorder(tree[root.left])
    if(root.right != "."):
        preorder(tree[root.right])

# 2) inorder
def inorder(root:Node):
    if(root.left != "."):
        inorder(tree[root.left])
    print(root.root, end="")
    if(root.right != "."):
        inorder(tree[root.right])
        
# 3) postorder
def postorder(root:Node):
    if(root.left != "."):
        postorder(tree[root.left])
    if(root.right != "."):
        postorder(tree[root.right])
    print(root.root, end="")

preorder(tree["A"])
print()
inorder(tree["A"])
print()
postorder(tree["A"])
