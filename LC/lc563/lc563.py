# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def lrn(node):
    if not node: return 0, 0
    v = node.val
    vl, tleftSum = lrn(node.left)
    vr, trightSum = lrn(node.right)
    return (v+vl+vr, tleftSum + trightSum+abs(vl-vr))
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        return lrn(root)[1]