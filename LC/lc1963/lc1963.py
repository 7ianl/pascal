class Solution:
    def minSwaps(self, s: str) -> int:
        openings = 0
        unmatched = 0
        for i in range(len(s)):
            if s[i] == "[":
                openings += 1
            else:
                if openings == 0:
                    unmatched += 1
                else:
                    openings -= 1
        return unmatched//2 + unmatched%2