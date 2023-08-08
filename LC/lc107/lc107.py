# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
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
            res.append(acc)
            level = nextlevel
        res.reverse()
        return res
        