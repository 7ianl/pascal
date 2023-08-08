class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numbers = dict()
        Counts = dict()
        for x in list(dict.fromkeys(nums)):
            Counts.update({x : nums.count(x)})
        nums = []
        for k, v in Counts.items():
            if v <= 3:
                nums.extend([k] * v)
            else:
                nums.extend([k] * 3)
        l = len(nums)
        output = list()
        for i in range(l):
            numbers.update({nums[i]:i})
        for i in range(l):
            for j in range (i, l):
                k = -(nums[i]+nums[j])
                if k in numbers and i != j:
                    if numbers[k] != i and numbers[k] != j:
                        Tuple = sorted([nums[i], nums[j], k])
                        if Tuple not in output:
                            output.append(Tuple)                            
        return output