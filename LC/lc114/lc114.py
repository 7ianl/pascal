# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def nlr(t):
            if not t: return
            l, r = t.left, t.right
            t.left = None
            nlr(l)
            nlr(r)
            t.right = l
            while t.right:
                t = t.right
            t.right = r
            return
        nlr(root)