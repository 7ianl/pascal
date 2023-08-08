class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        c = image[sr][sc]
        if c == newColor: return image
        def dfs(a, b):
            if not(0<=a and a<m and 0<=b and b<n and image[a][b] == c): return
            image[a][b] = newColor
            dfs(a-1, b)
            dfs(a+1, b)
            dfs(a, b-1)
            dfs(a, b+1)
        dfs(sr, sc)
        return image