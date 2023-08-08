class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        remaining = len(nums) - k
        stack = list()
        for n in nums:
            while stack and n < stack[-1] and remaining > 0:
                stack.pop()
                remaining -= 1
            stack.append(n)
        return stack[:k]
            
        