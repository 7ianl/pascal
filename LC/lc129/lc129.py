# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        global s
        s= 0
        def dfs(t, n):
            global s
            n = t.val + n*10
            if not t.left and not t.right: 
                s += n
                return
            if t.left:
                dfs(t.left, n)
            if t.right:
                dfs(t.right, n)
        dfs(root, 0)
        return s