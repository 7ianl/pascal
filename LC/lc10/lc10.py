# Not Intended Solution

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.compile('^'+p+'$').match(s) is not None