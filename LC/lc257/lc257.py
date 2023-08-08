# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(root):
            if not(root.left) and not(root.right):
                return [str(root.val)]
            acc = str(root.val)+"->"
            if not(root.left):
                return [acc + i for i in helper(root.right)]
            if not(root.right):
                return [acc + i for i in helper(root.left)]
            res = [acc + i for i in helper(root.left)]
            res.extend([acc + i for i in helper(root.right)])
            return res
        return helper(root)