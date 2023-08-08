class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        L = max(milestones)
        T = sum(milestones)
        if L * 2 > T:
            return (T-L)*2+1
        else:
            return T