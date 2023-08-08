# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            if root.val == sum:
                return True
            return False
        b1 = False if not root.left else self.hasPathSum(root.left, sum - root.val)
        b2 = False if not root.right else self.hasPathSum(root.right, sum - root.val)
        return b1 or b2