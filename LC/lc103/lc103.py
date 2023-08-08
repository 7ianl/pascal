# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        rev = False
        level = [root] if root else []
        while level:
            acc = []
            nextlevel = []
            for x in level:
                acc.append(x.val)
                if x.left:
                    nextlevel.append(x.left)
                if x.right:
                    nextlevel.append(x.right)
            if rev:
                acc.reverse()
            rev = not rev
            res.append(acc)
            level = nextlevel
        return res