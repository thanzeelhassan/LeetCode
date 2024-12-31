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
        r = n
        l = 1
        while(l<=r):
            mid = int(l + (r-l)/2)
            if isBadVersion(mid)==False:
                l = mid+1
            else:
                r = mid-1
        return l
