class Solution:    
    def minOperations(self, nums: List[int]) -> int:
        def flip(nums, i):
            nums[i] = 1 - nums[i]
            nums[i + 1] = 1 - nums[i + 1]
            nums[i + 2] = 1 - nums[i + 2]
            return nums
            
        n = len(nums)
        i = 0
        count = 0
        while (i < n - 2) :
            if nums[i] == 0:
                nums = flip(nums, i)
                count = count + 1
            
            i = i + 1

        if nums[i] == 1 and nums[i+1] == 1:
            return count
        return -1
