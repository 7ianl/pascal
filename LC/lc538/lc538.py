# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        global res
        res = 0
        def convert_aux(root):
            global res
            if not root:
                return None
            root.right = convert_aux(root.right)
            root.val += res
            res = root.val
            root.left = convert_aux(root.left)
            return root
        return convert_aux(root)