class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_path_present(root, seq, index=0):
    if root is None:
        return

    if index == len(seq) - 1 and seq[index] == root.val:
        return True

    return is_path_present(root.left, seq, index + 1) or is_path_present(root.right, seq, index + 1)


# Example
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(8)

arr1 = [5, 2, 4]
arr2 = [5, 3, 4, 9]

print("Path Exist" if is_path_present(root, arr1) else "Path does not Exist")
print("Path Exist" if is_path_present(root, arr2) else "Path does not Exist")
