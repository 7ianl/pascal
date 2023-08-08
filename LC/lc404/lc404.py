# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        global s
        s = 0
        def dfs(t, f):
            global s
            if not t: return
            if f and not t.left and not t.right: 
                s += t.val
                return
            dfs(t.left, True)
            dfs(t.right, False)
        dfs(root, False)
        return s