# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(preord, inord):
            if len(preord)==0: return None
            t = TreeNode(preord[0])
            for p in range(len(inord)):
                if inord[p] == preord[0]:
                    break
            t.left=helper(preord[1:p+1], inord[:p])
            t.right=helper(preord[p+1:], inord[p+1:])
            return t
        return helper(preorder, inorder)