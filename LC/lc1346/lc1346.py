class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for x in arr:
            if not x%2:
                if x/2 in seen:
                    return True
            if x * 2 in seen:
                return True
            seen.add(x)
        return False
        