class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i = 0
        L = len(nums)
        while i < L and nums[i] == 0:
            i += 1
        s = i
        i += 1
        while i < L:
            if nums[i] == 0:
                i += 1
            else:
                if (i-s) > k:
                    s = i
                    i += 1
                else:
                    return False
        return True
        