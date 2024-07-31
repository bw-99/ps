import sys
input = sys.stdin.readline

N = int(input())

class Node():
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right
        
tree={}
for _ in range(N):
    name, left, right = map(str, input().split())
    tree[name] = Node(name, left, right)

def preorder(node):
    print(node.name, end = '')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])
        
def inorder(node):
    if(node.left != "."):
        inorder(tree[node.left])
    print(node.name, end="")
    if(node.right != "."):
        inorder(tree[node.right])

def postorder(node):
    if(node.left != "."):
        postorder(tree[node.left])
    if(node.right != "."):
        postorder(tree[node.right])
    print(node.name, end="")

preorder(tree["A"])
print()
inorder(tree["A"])
print()
postorder(tree["A"])
