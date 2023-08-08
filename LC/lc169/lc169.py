class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem = 0
        count = 0
        for x in nums:
            if count == 0:
                elem = x
            if x == elem:
                count += 1
            else:
                count -= 1
        return elem