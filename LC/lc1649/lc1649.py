from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        Ins = SortedList()
        ans = 0
        for i in instructions:
            ans += min(Ins.bisect_left(i), len(Ins)-Ins.bisect_right(i))
            Ins.add(i)
            ans %= (10**9+7)
        return ans