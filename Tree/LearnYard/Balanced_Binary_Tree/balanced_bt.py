def height_bt(root):
    if root is None:
        return 0
    lh = height_bt(root.left)
    if lh == -1:
        return -1
    rh = height_bt(root.right)
    if rh == -1:
        return -1
    if abs(lh - rh) > 1:
        return -1
    return 1 + max(lh, rh)


def isBalanced(root) -> bool:

    if height_bt(root) == -1:
        return False
    return True
