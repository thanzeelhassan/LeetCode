class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 :
                neg = neg + 1
            elif nums[i] > 0:
                pos = pos + 1
        
        return max(neg, pos)
