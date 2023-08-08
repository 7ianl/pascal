class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        rowflag, colflag = False, False
        for i in range(cols):
            if matrix[0][i] == 0:
                rowflag = True
                break
        for j in range(rows):
            if matrix[j][0] == 0:
                colflag = True
                break
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0
        for i in range(1, rows):
            if matrix[i][0] == 0:
                matrix[i] = [0]*cols
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0
        if rowflag:
            matrix[0] = [0]*cols
        if colflag:
            for i in range(1, rows):
                    matrix[i][0] = 0