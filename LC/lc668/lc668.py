class Solution:
    
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        if m > n:
            m, n = n, m
        lo, hi = 1, m*n
        
        while lo < hi:
            mid = (lo+hi-1)//2
            res = sum(min(mid//i, n) for i in range(1,m+1))
            if res >= k:
                hi = mid
            else:
                lo = mid+1
        return lo