class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = dict()
        for x in ransomNote:
            if x not in letters:
                letters[x] = 1
            else:
                letters[x] += 1
        for x in letters:
            if magazine.count(x) < letters[x]:
                return False
        return True
        