class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        out = [intervals[0]]
        for i in range(1,len(intervals)):
            e1 = out[-1][1]
            s2 = intervals[i][0]
            e2 = intervals[i][1]
            if s2 <= e1:
                if e1 < e2:
                    out[-1][1] = e2
                else:
                    continue
            else:
                out.append(intervals[i])
        return out
