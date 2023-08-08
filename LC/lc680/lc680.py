class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(s):
            lo, hi = 0, len(s)-1
            while lo <= hi:
                if s[lo] != s[hi]:
                    return False
                lo += 1
                hi -= 1
            return True
        lo, hi = 0, len(s)-1
        while lo <= hi:
            if s[lo] == s[hi]:
                lo += 1
                hi -= 1
            else:
                break
        if lo >= hi:
            return True
        else:
            s1 = s[:lo]+s[lo+1:]
            s2 = s[:hi]+s[hi+1:]
        return helper(s1) or helper(s2)