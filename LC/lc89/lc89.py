class Solution:
    def grayCode(self, n: int) -> List[int]:
        def helper(arr):
            l = len(arr)
            for i in range(l, 0, -1):
                arr.append(arr[i-1] + l)
        res = [0]
        for j in range(n):
            helper(res)
        return res
                