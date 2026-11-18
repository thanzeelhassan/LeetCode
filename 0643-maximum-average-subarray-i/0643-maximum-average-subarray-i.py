class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = sum(nums[0:k])
        current_sum = max_sum
        n = len(nums)
        for i in range(k, n):
            current_sum = current_sum + nums[i] - nums[i-k]
            max_sum = max(max_sum, current_sum)
        
        return max_sum / k