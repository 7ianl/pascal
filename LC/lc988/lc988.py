# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def conv(n):
            return chr(n+97)
        def helper(root):
            acc = conv(root.val)
            if not root.left and not root.right: return [acc]
            if not root.left:
                return [i+acc for i in helper(root.right)]
            if not root.right:
                return [i+acc for i in helper(root.left)]
            left = [i+acc for i in helper(root.left)]
            right = [i+acc for i in helper(root.right)]
            left.extend(right)
            return left
        res = helper(root)
        res.sort()
        return res[0]