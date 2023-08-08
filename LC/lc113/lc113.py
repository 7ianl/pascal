# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        def pathHelper(root, acc, target):
            acc.append(root.val)
            acc2 = acc[:]
            if not root.left and not root.right:
                if root.val == target:
                    res.append(acc)
            if root.left:
                pathHelper(root.left, acc, target - root.val)
            if root.right:
                pathHelper(root.right, acc2, target - root.val)

        pathHelper(root, [], sum)
        return res
        