# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum, cur_sum=0):

        if root is None:
            return
        cur_sum += root.val
        if root.left is None and root.right is None:
            if cur_sum == targetSum:
                return True

        return self.hasPathSum(root.left, targetSum, cur_sum) or self.hasPathSum(root.right, targetSum, cur_sum)
