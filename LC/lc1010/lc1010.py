class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        h = [0]*60
        for t in time:
            h[t%60]+=1
        res = 0
        for i in range(1, 30):
            res += h[i]*h[60-i]
        for i in [0, 30]:
            if h[i] >= 2:
                res += h[i]*(h[i]-1)//2
        return res