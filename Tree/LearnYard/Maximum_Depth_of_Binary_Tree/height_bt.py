
def maxDepth(root):
    if root is None:
        return 0
    lh = maxDepth(root.left)
    rh = maxDepth(root.right)
    return 1+ max(lh, rh)

