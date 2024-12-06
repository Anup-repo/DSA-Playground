class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root, result):
    if root is None:
        return
    inorder(root.left,result)
    result.append(root.val)
    inorder(root.right,result)

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
inorder(root, result)
print(result)
