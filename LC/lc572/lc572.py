# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfsChecker(t1, t2):
            if not t1 and not t2: return True
            if not t1 or not t2: return False
            return t1.val == t2.val and dfsChecker(t1.left, t2.left) and dfsChecker(t1.right, t2.right)
        def dfs(t):
            if not t: return False
            if dfsChecker(t, subRoot): return True
            return dfs(t.left) or dfs(t.right)
        return dfs(root)