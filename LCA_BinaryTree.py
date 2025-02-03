class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):
    # Base case: if root is None or equal to either p or q
    if root is None or root.val == p.val or root.val == q.val:
        return root

    # Recursively search in left and right subtrees
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    # If both left and right are non-null, root is the LCA
    if left and right:
        return root

    # Otherwise, return the non-null value
    return left if left else right


root = TreeNode(1)
root.left = 2
root.right = 3

lca = lowestCommonAncestor(root, node1, node2)
