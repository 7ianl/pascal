class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = len(nums)
        d = 100000
        for i, v in enumerate(nums[:-2]):
            if i > 1 and v == nums[i-1]:
                continue
            else:
                k = target - v
                left = i + 1
                right = l - 1
                while left < right:
                    if nums[left] + nums[right] < k:
                        d = min([d, k - nums[left] - nums[right]], key = abs)
                        left += 1
                    else:
                        d = min([d, k - nums[left] - nums[right]], key = abs)
                        right -= 1
        return target - d