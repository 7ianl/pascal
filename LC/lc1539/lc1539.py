class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        res = 1
        while True:
            if res in arr:
                res += 1
            else:
                k -= 1
                if k <= 0:
                    break
                res += 1
        return res