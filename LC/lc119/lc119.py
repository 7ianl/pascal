class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]*(rowIndex+1)
        for i in range(1, rowIndex+1):
            new = res[:]
            for j in range(1, i):           
                new[j] = res[j] + res[j-1]
            res = new
        return res
                