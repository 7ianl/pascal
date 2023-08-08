class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = set(nums1)
        x.intersection_update(set(nums2))
        return x