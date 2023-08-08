class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        c = max(candies)
        res = []
        for i in candies:
            res.append(i+extraCandies>=c)
        return res