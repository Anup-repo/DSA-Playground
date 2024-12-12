def minDepth(root) -> int:
    if root is None:
        return 0
    lh = self.minDepth(root.left)
    rh = self.minDepth(root.right)
    if not root.left or not root.right:
        return 1 + max(lh, rh)
    return 1 + min(lh, rh)


