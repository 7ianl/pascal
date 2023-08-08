# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l < r:
            p = (r-l)//2 + l
            if isBadVersion(p):
                r = p-1
            else:
                l = p+1
        if isBadVersion(r):
            return r
        return r + 1