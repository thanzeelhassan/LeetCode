class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        sum_total = sum(nums)
        sum_left = 0
        sum_right = sum_total
        count = 0

        for i in range(0, len(nums)):

            if nums[i] == 0 and sum_left == sum_right :
                count = count + 2
            elif nums[i] == 0 and abs(sum_left - sum_right) <= 1 :
                count = count + 1
            
            sum_left = sum_left + nums[i]
            sum_right = sum_right - nums[i]
            
        return count
