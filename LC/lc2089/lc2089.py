class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        if target not in nums: return res
        heapq.heapify(nums)
        i = 0
        while nums:
            p = heapq.heappop(nums)
            if p > target: 
                break
            elif p == target:
                res.append(i)
            i += 1
        return res