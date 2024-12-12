def left_height(root):
    height = 0
    while root:
        height += 1
        root = root.left
    return height

def right_height(root):
    height = 0
    while root:
        height += 1
        root = root.right
    return height   

def countNodes(root):
    if root is None:
        return 0

    lh = left_height(root)
    rh = right_height(root)

    if lh == rh:
        return (1 << lh) - 1  # Complete binary tree formula: 2^height - 1

    # Recursively count nodes in left and right subtrees
    return 1 + countNodes(root.left) + countNodes(root.right)
