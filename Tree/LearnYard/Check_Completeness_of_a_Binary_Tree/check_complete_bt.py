def is_complete_binary_tree(root):
    if not root:
        return True 

    queue = []
    queue.append(root)

    encountered_non_full = False

    while queue:
        current = queue.pop(0)

        if current.left:
            if encountered_non_full:
                return False
            queue.append(current.left)
        else:
            encountered_non_full = True

        if current.right:
            if encountered_non_full:
                return False
            queue.append(current.right)
        else:
            encountered_non_full = True

    return True
