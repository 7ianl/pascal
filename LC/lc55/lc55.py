class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 1
        solutions = set()
        solutions.add(i)
        if i >= 25000:
            return False
        i -= 1
        while i >= 0:
            k = nums[i]
            for j in range(1, k+1):
                if i + j in solutions:
                    solutions.add(i)
                    break
            i -= 1
        if 0 in solutions:
            return True
        else:
            return False
            
        