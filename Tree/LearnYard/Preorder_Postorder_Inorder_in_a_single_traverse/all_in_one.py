class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_in_post_traversal(root):
    pre_order , in_order, post_order = [], [], []

    if root is None: return pre_order, in_order, post_order

    stack = [(root,1)] # initialize stack with root value and state 1

    while stack:
        node, state = stack.pop()
        if state == 1: # preform pre-order traveral
            pre_order.append(node.val)
            state = 2
            stack.append((node,state))
            if node.left:
                stack.append((node.left,1))

        elif state == 2: # perform in-order traveral
            in_order.append(node.val)
            state = 3
            stack.append((node,state))
            if node.right:
                stack.append((node.right,1))

        else: # perform post-order traveral
            post_order.append(node.val)
    return pre_order, in_order, post_order

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

pre,in_order, post = pre_in_post_traversal(root)
print("Pre-order",pre)
print("In-order",in_order)
print("Post-order",post)
