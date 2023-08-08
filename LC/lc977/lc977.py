class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def merge(a, b):
            L1, L2 = len(a), len(b)
            p1, p2 = 0, 0
            res = list()
            while p1 < L1 and p2 < L2:
                if a[p1] < b[p2]:
                    res.append(a[p1])
                    p1 += 1
                else:
                    res.append(b[p2])
                    p2 += 1
            if p1 < L1:
                res.extend(a[p1:])
            if p2 < L2:
                res.extend(b[p2:])
            return res
        p = 0
        def square(x): return x*x
        while p < len(nums) and nums[p]<0:
            p+= 1
        return merge(list(map(square, reversed(nums[:p]))), list(map(square,nums[p:])))
             