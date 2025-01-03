class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = 0
        left_sum = 0
        right_sum = sum(nums)
        n = len(nums)
        for i in range(0, n-1):
            left_sum = left_sum + nums[i]
            right_sum = right_sum - nums[i]
            if left_sum >= right_sum:
                ans = ans + 1
            
        return ans
