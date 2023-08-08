class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        r = 0
        for x in operations:
            if x[1]=='+':
                r += 1
            else:
                r -= 1
        return r