# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def maxDepth(tree):
            if not tree:
                return 0
            return max(maxDepth(tree.left), maxDepth(tree.right)) + 1
        if not root:
            return True
        i = maxDepth(root.left)
        j = maxDepth(root.right)
        if abs(i - j) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)