class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        lo, hi = sum(quantities)//n, max(quantities)
        while lo < hi:
            mid = (lo+hi)//2
            if mid <= 0:
                lo = mid +1
                continue
            count = 0
            for x in quantities:
                if x%mid:
                    count += (x//mid+1)
                else:
                    count += x//mid
            if count > n:
                lo = mid + 1
            else:
                hi = mid
        return hi