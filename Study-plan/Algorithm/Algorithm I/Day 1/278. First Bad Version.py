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
        start = 1
        end = n
        while start <= end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                if isBadVersion(mid -1):
                    end = mid
                else:
                    return mid
            else:
                if isBadVersion(mid + 1):
                    return mid + 1
                else:
                    start = mid + 1
