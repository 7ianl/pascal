class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        t = set()
        for c in nums:
            if c in t:
                return True
            t.add(c)
        return False