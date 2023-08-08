class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            result =""
            cycle = numRows * 2 - 2
            List = [""] * numRows
            for i in range(len(s)):
                if i % (2 * numRows - 2) < numRows - 1:
                    k = i%(2 *numRows - 2)
                else:
                    k = (numRows - 1) - (i % (2*numRows-2) -(numRows -1))
                List[k] += s[i]
            for x in List:
                result += x
            return result