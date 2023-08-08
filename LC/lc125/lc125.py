class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isPalindromeAux(s):
            lo, hi = 0, len(s) -1
            while lo <= hi:
                if s[lo].lower() != s[hi].lower():
                    return False
                lo+=1
                hi-=1
            return True
        p = set(list(range(65,91))+list(range(97,123))+list(range(48,58)))
        L = list(filter(lambda c : ord(c) in p, list(s)))
        return isPalindromeAux(L)