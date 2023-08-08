class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)
        def cmp(a, b):
            return (a > b) - (a < b)

        def turn(p, q, r):
            return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

        def _keep_left(hull, r):
            while len(hull) > 1 and turn(hull[-2], hull[-1], r) == TURN_RIGHT:
                hull.pop()
            if not len(hull) or hull[-1] != r:
                hull.append(r)
            return hull

        trees = sorted(trees)
        l = reduce(_keep_left, trees, [])
        u = reduce(_keep_left, reversed(trees), [])
        res= l.extend(u[i] for i in range(1, len(u) - 1)) or l
        res.sort()
        return list(res for res,_ in itertools.groupby(res))