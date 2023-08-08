class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = {0:(nums[0], True)}
        if nums[1] > nums[0]:
            dp[1] = (nums[1], True)
        else:
            dp[1] = (nums[0], False)
        k = len(nums) - 1
        for i in range(2, k+1):
            if dp[i-1][1] == False:
                dp[i] = (dp[i-1][0] + nums[i], True)
            else:
                left = dp[i-2][0] + nums[i]
                right = dp[i-1][0]
                if left >= right:
                    dp[i] = (left, True)
                else:
                    dp[i] = (right, False)
        return dp[k][0]