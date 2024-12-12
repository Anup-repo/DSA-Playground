def height_bt(root):
    if root is None:
        return 0
    lh = height_bt(root.left)
    rh = height_bt(root.right)
    maxi[0] = max(maxi[0],lh+rh)
    return 1 + max(lh, rh)

def diameterOfBinaryTree(root):
    maxi = [0]
    height_bt(root)
    return maxi[0]
