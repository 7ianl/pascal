class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        k = sum(nums) - x
        if k == 0:
            return len(nums)
        sums = dict()
        maxlen = -1
        listsum = 0
        for i in range(len(nums)):
            listsum += nums[i]
            if listsum == k:
                maxlen = i + 1
            if listsum - k in sums:
                maxlen = max(maxlen, i - sums[listsum - k])
            if listsum not in sums:
                sums[listsum] = i
        if maxlen == -1:
            return -1
        return len(nums) - maxlen
        