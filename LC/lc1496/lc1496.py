class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set()
        loc = (0, 0)
        seen.add(loc)
        for i in range(len(path)):
            x = loc[0]; y = loc[1]
            if path[i] == 'N':
                y += 1
            elif path[i] == 'S':
                y -= 1
            elif path[i] == 'E':
                x -= 1
            else:
                x += 1
            loc = (x, y)
            if loc in seen:
                return True
            seen.add(loc)
        return False
        