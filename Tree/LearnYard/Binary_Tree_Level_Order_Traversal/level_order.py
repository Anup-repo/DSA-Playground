class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    result = []
    if root is None:
        return result
    queue = deque([root])

    while queue:
        temp = []
        for _ in range(len(queue)):
            ele = queue.popleft()
            if ele.left:
                queue.append(ele.left)
            if ele.right:
                queue.append(ele.right)
            temp.append(ele.val)
        result.append(temp)

    return result

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

result = levelOrder(root)
print(result)
