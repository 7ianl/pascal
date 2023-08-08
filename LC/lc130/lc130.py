class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def loc(r, c):
            res = []
            if r > 0 and c >= 0 and c<n: 
                res.append((r-1, c))
            if r < m-1 and c >= 0 and c<n:
                res.append((r+1, c))
            if c > 0 and r>=0 and r<m:
                res.append((r, c-1))
            if c < n-1 and r>=0 and r<m:
                res.append((r, c+1))
            return res
        def bfs(cur):
            nxt = []
            for r, c in cur:
                for x, y in loc(r, c):
                    if board[x][y] == 'O':
                        nxt.append((x, y))
                        board[x][y] = 'P'
            if len(nxt) == 0: return
            return bfs(nxt)
        init = list(zip([-1]*n+list(range(m))+[m]*n+list(range(m)), list(range(n))+[-1]*m+list(range(n))+[n]*m))
        bfs(init)
        for i in range(m*n):
            if board[i//n][i%n] == 'O':
                board[i//n][i%n] = 'X'
        for i in range(m*n):
            if board[i//n][i%n] == 'P':
                board[i//n][i%n] = 'O'