class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        for i in range(n-2, -1, -1):
            shifts[i] += shifts[i+1]
            
        ans = []
        for i, c in enumerate(s):
            idx = (ord(c) - ord('a') + shifts[i]) % 26
            ans.append(chr(idx + ord('a')))
        return "".join(ans)
        