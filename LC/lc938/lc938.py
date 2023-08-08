# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(t):
            if not t: return 0
            res = 0
            if low <= t.val and t.val <= high:
                res += t.val
            res += dfs(t.left)
            res += dfs(t.right)
            return res
        return dfs(root)