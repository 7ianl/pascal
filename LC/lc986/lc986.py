class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        while firstList and secondList:
            (a, b), (c, d) = firstList[-1], secondList[-1]
            if a > d:
                firstList.pop()
            elif c > b:
                secondList.pop()
            elif a >= c:
                res.append([a, min(b, d)])
                firstList.pop()
            else:
                res.append([c, min(b, d)])
                secondList.pop()
        res.reverse()
        return res
                