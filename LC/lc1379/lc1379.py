# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        targetInt = target.val
        def getUniqueNode(cloned: TreeNode, targetInt) -> TreeNode:
            if cloned == None:
                return None
            elif cloned.val == targetInt:
                return cloned
            elif getUniqueNode(cloned.left, targetInt) != None:
                return getUniqueNode(cloned.left, targetInt)
            else:
                return getUniqueNode(cloned.right, targetInt)
        return getUniqueNode(cloned, targetInt)
        