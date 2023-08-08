class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        p, q = nums.index(min(nums)), nums.index(max(nums))
        if q < p:
            p, q = q, p
        if p == q: return 1
        a, b, c = p, q-p-1, len(nums)-q-1
        return min(a+b+2, a+c+2, b+c+2)