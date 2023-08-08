class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        options = [i+1 for i in range(n)]
        divisor = 1
        for x in range(1, n):
            divisor *= x
        result = []
        while True:
            nxt = (k-1)//divisor
            result.append(str(options.pop(nxt)))
            k -= divisor*nxt
            try:
                divisor //= len(options)
            except:
                break
            
        return ''.join(result)