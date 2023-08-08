def gcd(a, b): return a if b == 0 else gcd(b, a%b)
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        lo, hi = 2, min(a, b)*n
        f = a*(b//gcd(a, b))
        while lo <= hi:
            mid = (lo+hi)//2
            k = mid//a + mid//b - mid//f
            if k < n:
                lo = mid+1
            elif k == n and (mid%a == 0 or mid%b == 0): return mid%(10**9+7)
            else:
                hi = mid-1
        return lo%(10**9+7)