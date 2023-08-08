# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pval, qval = p.val, q.val
        def inSub(t, n):
            if t.val == n:
                return True
            elif not t.left and not t.right:
                return False
            elif not t.left:
                return inSub(t.right, n)
            elif not t.right:
                return inSub(t.left, n)
            return inSub(t.left, n) or inSub(t.right, n)
        def inLeftSub(t, n):
            if not t.left:
                return False
            elif t.left.val == n:
                return True
            else:
                return inSub(t.left, n)

        def helper(t):
            if t.val == pval or t.val == qval:
                return t
            t1, t2 = inLeftSub(t, pval), inLeftSub(t, qval)
            if t1 != t2:
                return t
            elif t1:
                return helper(t.left)
            else:
                return helper(t.right)
        return helper(root)