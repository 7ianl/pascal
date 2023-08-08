class Solution:
    def nthUglyNumber(self, n: int) -> int:
        arr, dp2, dp3, dp5 = [1], 0, 0, 0
        for i in range(n-1):
            p2, p3, p5 = arr[dp2]*2, arr[dp3]*3, arr[dp5]*5
            k = min(p2, p3, p5)
            arr.append(k)
            if k == p2:
                dp2 += 1
            if k == p3:
                dp3 += 1
            if k == p5:
                dp5 += 1
        return arr[-1]
        