class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root, result):
    if root == None:
        return
    result.append(root.val)
    preorder(root.left, result)
    preorder(root.right, result)

# Creating a sample binary tree
#       1
#      / \
#     2   3
#    / \
#   4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

result = []
preorder(root, result)
print(result)