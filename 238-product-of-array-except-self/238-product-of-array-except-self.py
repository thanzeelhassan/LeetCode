class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_array = [1]*n
        for i in range(n-2,-1,-1):
            prefix_array[i] = prefix_array[i+1] * nums[i+1]        
        x = 1
        y = 1
        for i in range(0,n):
            y = x * prefix_array[i]
            x = x * nums[i]
            nums[i] = y               
        return nums        