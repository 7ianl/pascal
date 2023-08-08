# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(t):
            if not t: return 0
            return max(depth(t.left), depth(t.right))+1
        def dfs(t):
            if not t: return 0
            k = depth(t.left) + depth(t.right)
            return max(k, dfs(t.left), dfs(t.right))
        return dfs(root)