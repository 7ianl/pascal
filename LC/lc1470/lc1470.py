class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        p=0
        res = []
        while p <n:
            res.append(nums[p])
            res.append(nums[p+n])
            p+=1
        return res