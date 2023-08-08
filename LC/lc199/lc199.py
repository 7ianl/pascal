# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def levelTraversal(root):
            branches = [root]
            res = list()
            while branches:
                temp = list()
                level = list()
                for x in branches:
                    if x.left:
                        temp.append(x.left)
                    if x.right:
                        temp.append(x.right)
                    level.append(x.val)
                res.append(level)
                branches = temp
            return res
        res = list()
        if not root:
            return res
        levels = levelTraversal(root)
        for x in levels:
            res.append(x[-1])
        return res
                        