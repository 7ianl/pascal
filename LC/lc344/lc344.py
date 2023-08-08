class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rev_helper(i):
            if i >= len(s)//2:
                return
            else:
                s[i], s[-1-i] = s[-1-i], s[i]
                return rev_helper(i+1)
        rev_helper(0)