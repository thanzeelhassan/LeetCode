class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_array = [1]*n
        temp = 1
        for i in range(n-2,-1,-1):
            prefix_array[i] = prefix_array[i+1] * nums[i+1]        
        x = 1
        y = 1
        for i in range(0,n):
            temp = prefix_array[i]
            y = x * temp
            x = x * nums[i]
            nums[i] = y               
        return nums        