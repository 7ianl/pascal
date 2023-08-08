class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = dict()
        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
        p = [(x, y) for x, y in freq.items()]
        p.sort()
        res = list()
        for i in range(len(p)-1):
            if p[i][0] + 1 == p[i+1][0]:
                res.append(p[i][1]+p[i+1][1])
        if not res:
            return 0
        else:
            return max(res)
        