# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(t, v):
            if not t: return 0
            res = int(t.val >=v)
            res+=dfs(t.left, max(t.val, v))
            res+=dfs(t.right,max(t.val, v))
            return res
        return dfs(root, root.val)