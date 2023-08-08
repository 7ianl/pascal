class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText)//rows
        mat = []
        for i in range(1, cols+1):
            mat.append([x for x in encodedText[cols*(i-1):cols*i]])
        col = 0
        res = []
        while col < cols:
            a, b = 0, col
            while a < rows and b < cols:
                res.append(mat[a][b])
                a+=1
                b+=1
            col += 1
        return ''.join(res).rstrip()