class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        if start == goal: return 0
        this, seen, level = [start], set(), 0
        while len(this):
            nxt = []
            level += 1
            for x in this:
                for y in nums:
                    for k in (x-y, x+y, x^y):
                        if k == goal: return level
                        elif (k in seen or k<0 or k>1000): 
                            continue
                        else:
                            seen.add(k)
                            nxt.append(k)
            this = nxt
        return -1
                            
                        