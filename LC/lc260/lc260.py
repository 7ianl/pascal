class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        h = set()
        for i in nums:
            if i not in h:
                h.add(i)
            else:
                h.remove(i)
        return list(h)