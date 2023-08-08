def sqrdst(p, q): return abs(p[0]-q[0])**2 + abs(p[1]-q[1])**2
def slope(x1, y1, x2, y2): 
    try:
        return (y2-y1)/(x2-x1)
    except:
        return float('inf')
def midpoint(p, q): return (p[0]+q[0])/2, (p[1]+q[1])/2
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        arr = [p1, p2, p3, p4]
        arr.sort(key=lambda x : x[0])
        arr.sort(key=lambda x : x[1])
        if sqrdst(arr[0], arr[3]) != sqrdst(arr[1], arr[2]): return False
        a, b = midpoint(arr[0], arr[3])
        c, d = midpoint(arr[1], arr[2])
        if not math.isclose(a, c) or not math.isclose(b, d): return False
        res = slope(*arr[0], *arr[3]) * slope(*arr[1], *arr[2])
        return math.isclose(res, -1) if res < float('inf') else res != float('inf')