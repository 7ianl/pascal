class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        p = 10**9 + 7
        L = len(nums)
        count0, count1,count2 = 0, 0, 0
        for i in range(L):
            if nums[i] == 0:
                count0 = (count0*2 +1)%p
            elif nums[i] == 1:
                count1 = (count1*2 + count0)%p
            else:
                count2 = (count2*2 + count1)%p
        return count2