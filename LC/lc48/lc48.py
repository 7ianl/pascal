class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        i = n**2//4
        l = n//2 + n%2
        for p in range(i):
            r, c = p//l, p%l
            n1, n2, n3, n4 = matrix[r][c], matrix[c][n-r-1], matrix[n-r-1][n-c-1], matrix[n-c-1][r]
            matrix[r][c], matrix[c][n-r-1], matrix[n-r-1][n-c-1], matrix[n-c-1][r] = n4, n1, n2, n3
        return