# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(tree1, tree2):
            if not (tree1 or tree2):
                return True
            if not (tree1 and tree2):
                return False
            if tree1.val != tree2.val:
                return False
            return isMirror(tree1.left, tree2.right) and isMirror(tree1.right, tree2.left)
        if not root:
            return True
        return isMirror(root.left, root.right)
        