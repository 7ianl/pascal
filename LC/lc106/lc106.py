# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(i1, i2, p1, p2):
            if p1>=p2: return None
            k = postorder[p2-1]
            res = TreeNode(k)
            p = inorder.index(k)
            res.left = helper(i1, p, p1, p1-i1+p)
            res.right = helper(p+1, i2, p1-i1+p, p2-1)
            return res
        L = len(inorder)
        return helper(0, L, 0, L)