# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        L = len(nums)
        i = L // 2
        val = nums[i]
        left = self.sortedArrayToBST(nums[:i])
        right = self.sortedArrayToBST(nums[i+1:])
        return TreeNode(val, left, right)
        