class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        for n in sorted(nums,reverse=True):
            if n < 0:
                return -1
            if -n in s:
                return n
        return -1