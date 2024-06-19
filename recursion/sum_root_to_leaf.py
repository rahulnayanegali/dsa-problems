# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root, num=0):

        if root is None:
            return 0
        if root.left is None and root.right is None:
            return int(str(num) + str(root.val))

        return self.sumNumbers(root.left, str(num) + str(root.val)) + self.sumNumbers(root.right, str(num) + str(root.val))
