class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def ascsearch(nums, target):
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
                elif nums[i] > target:
                    return -1
                else:
                    continue
            return -1
        index = 0
        while index < len(nums) - 1:
            if nums[index] < nums[index+1]:
                index += 1
            else:
                break
        k = ascsearch(nums[:index+1],target)
        if k != -1:
            return k
        else:
            k1 = ascsearch(nums[index+1:],target)
            if k1 == -1:
                return -1
            else:
                return index + 1 + k1