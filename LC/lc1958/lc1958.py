class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        rows, cols = len(board), len(board[0])
        def getColor(r, c):
            if r >= 0 and c >= 0 and r < rows and c < cols and board[r][c] != ".":
                return board[r][c]
            else: return None
        Left, Right, Up, Down = (0, -1), (0, 1), (-1, 0), (1, 0)
        LeftUp, LeftDown, RightUp, RightDown = (-1, -1), (1, -1), (-1, 1), (1, 1)
        def positionIncrement(t, r, c, moves):
            return getColor(r + t[0]*moves, c +t[1]*moves)
        def checkLegal(t, r, c, color):
            curMoves = 1
            mid = positionIncrement(t, r, c, curMoves)
            if not mid or mid == color: return False
            else:
                while True:
                    curMoves += 1
                    if positionIncrement(t, r, c, curMoves) == None:
                        return False
                    if positionIncrement(t, r, c, curMoves) != mid:
                        return True
        res = False
        for t in [Left, Right, Up, Down, LeftUp, LeftDown, RightUp, RightDown]:
            res = res or checkLegal(t, rMove, cMove, color)
        return res
                    
                    
            