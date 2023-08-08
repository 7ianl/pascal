class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        c = set()
        q = False
        for i, v in enumerate(arr):
            if v == 0:
                c.add(i)
            if v > 1:
                q = True
        if len(c) == 0:
            return False
        if not q:
            return True
        while True:
            flip = False
            for i, v in enumerate(arr):
                if v == 0: continue
                if i+v in c or i-v in c:
                    arr[i] = 0
                    c.add(i)
                    flip = True
            if not flip:
                break
        return start in c