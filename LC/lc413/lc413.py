class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        for i in range(len(A)-1):
            A[i] -= A[i+1]
        for j in range(len(A)-2):
            A[j] -= A[j+1]
        l = []
        c = 0
        for x in A[:-2]:
            if x == 0:
                c += 1
            else:
                l.append(c)
                c = 0
        l.append(c)
        res = 0
        for n in l:
            res += (n*(n+1))/2
        return int(res)