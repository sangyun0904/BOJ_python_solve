import sys
input = sys.stdin.readline

N = int(input())
b_tree = {}

for _ in range(N):
    nodes = input().strip().split()
    b_tree[nodes[0]] = nodes[1:]

root = "A"

def inorder(node):
    print(node, end="")
    if b_tree[node][0] != ".":
        inorder(b_tree[node][0])
    if b_tree[node][1] != ".":
        inorder(b_tree[node][1])

def preorder(node):
    if b_tree[node][0] != ".":
        preorder(b_tree[node][0])
    print(node, end="")
    if b_tree[node][1] != ".":
        preorder(b_tree[node][1])

def postorder(node):
    if b_tree[node][0] != ".":
        postorder(b_tree[node][0])
    if b_tree[node][1] != ".":
        postorder(b_tree[node][1])
    print(node, end="")

inorder(root)
print()
preorder(root)
print()
postorder(root)