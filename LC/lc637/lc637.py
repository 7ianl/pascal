# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        levels = []
        level = [root] if root else []
        while level:
            acc = 0
            counter = 0
            nextlevel = []
            for x in level:
                acc += x.val
                counter += 1
                if x.left:
                    nextlevel.append(x.left)
                if x.right:
                    nextlevel.append(x.right)
            levels.append(acc/counter)
            level = nextlevel
        return levels
        