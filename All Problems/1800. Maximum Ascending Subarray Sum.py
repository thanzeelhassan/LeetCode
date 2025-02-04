class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        current_sum = 0
        n = len(nums)
        if n == 1:
            return nums[0]
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                current_sum = current_sum + nums[i]
                continue
            else:
                if current_sum > max_sum:
                    max_sum = current_sum
                current_sum = nums[i]
        if current_sum > max_sum:
            max_sum = current_sum
        return max_sum
        