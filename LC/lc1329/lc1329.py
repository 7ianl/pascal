class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat); n = len(mat[0])
        elems = dict()
        for i in range(m):
            for j in range(n):
                k = i - j
                if k not in elems:
                    elems[k] = [mat[i][j]]
                else:
                    elems[k].append(mat[i][j])
        for x in elems.values():
            x.sort()
        for i in range(m):
            for j in range(n):
                mat[i][j] = elems[i-j].pop(0)
        return mat