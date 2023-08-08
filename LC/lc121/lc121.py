class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = list()
        for i in range(1,len(prices)):
            arr.append(prices[i] - prices[i-1])
        maxSoFar = 0
        maxCont = 0
        for i in range(len(arr)):
            maxCont = max(maxCont + arr[i], arr[i])
            maxSoFar = max(maxSoFar, maxCont)
        return maxSoFar
        