class Solution:
    def countPrimes(self, n: int) -> int:
        limit = math.floor(math.sqrt(n))
        nums = [True] * (n-2)
        L, p = len(nums), 0
        if L == 0: return 0
        while True:
            p += 1
            if p > limit:
                break
            if nums[p-1]:
                prime = p + 1
                for i in range(prime*prime, n, prime):
                    nums[i-2] = False
        return sum(nums)
            