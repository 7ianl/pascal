class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        left = 0
        up = [0]*n
        count = 0
        for i in range(len(grid)):
            left = 0
            for j in range(n):
                if grid[i][j] == 0:
                    up[j] = 0
                    left = 0
                else:
                    if not left and not up[j]:
                        count += 4
                    elif not left or not up[j]:
                        count += 2
                    left = 1
                    up[j] = 1
        return count
        