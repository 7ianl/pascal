# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        vals = []
        def lnr(t):
            if not t: return
            lnr(t.left)
            vals.append(t.val)
            lnr(t.right)
        lnr(root)
        l = list(set(vals))
        if len(l) <= 1: return -1
        heapq.heapify(l)
        heapq.heappop(l)
        return l[0]