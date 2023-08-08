class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def isBlocked(m, n):
            if obstacleGrid[-m][-n] == 1:
                return True
            else:
                return False
        ans = dict()
        if isBlocked(1, 1):
            return 0
        else:
            ans[(1, 1)] = 1
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(2, m+1):
            if isBlocked(i, 1):
                ans[(i, 1)] = 0
            else:
                ans[(i, 1)] = ans[(i-1, 1)]
        for i in range(2, n+1):
            if isBlocked(1, i):
                ans[(1, i)] = 0
            else:
                ans[(1, i)] = ans[(1, i-1)]
        for i in range(2, m+1):
            for j in range(2, n+1):
                if isBlocked(i, j):
                    ans[(i,j)] = 0
                else:
                    ans[(i, j)] = ans[(i-1, j)] + ans[(i, j-1)]
        return ans[(m, n)]