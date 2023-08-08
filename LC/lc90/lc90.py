class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsetSize, seen = 0, set()
        res = [[]]
        startingIndex = 0
        for x in nums:
            if x in seen:
                startingIndex = subsetSize
            else:
                startingIndex = 0
                seen.add(x)
            acc = []
            subsetSize = len(res)
            for i in range(startingIndex, subsetSize):
                acc.append(res[i]+[x])
            res.extend(acc)
        return res