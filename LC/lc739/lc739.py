class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        L = len(temperatures)
        res = [0]*L
        stack = []
        for i, j in enumerate(temperatures):
            while len(stack) > 0 and j > stack[-1][1]:
                p, q = stack.pop()
                res[p] = i - p
            stack.append((i, j))
        return res