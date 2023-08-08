# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        global prev, fst, snd
        prev, fst, snd= TreeNode(-10**10), None, None
        def lnr(root):
            global prev, fst, snd
            if not root: return
            lnr(root.left)
            if (fst == None and root.val < prev.val):
                fst = prev
            if (fst != None and root.val < prev.val):
                snd = root
            prev = root
            lnr(root.right)
        lnr(root)
        tmp = fst.val
        fst.val = snd.val
        snd.val = tmp
        return