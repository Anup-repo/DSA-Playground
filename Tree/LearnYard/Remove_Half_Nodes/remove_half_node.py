class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def RemoveHalfNodes(node): # post-order traversal used 
    # code here
    if node is None:
        return
    node.left = RemoveHalfNodes(node.left)
    node.right = RemoveHalfNodes(node.right)
    if node.left is None and node.right is not None:
        return node.right
    if node.left is not None and node.right is None:
        return node.left
    return node


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)


# Creating a sample binary tree
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6
#   /
#  7
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.left.left = Node(7)


node = RemoveHalfNodes(root)
inorder_traversal(node)
