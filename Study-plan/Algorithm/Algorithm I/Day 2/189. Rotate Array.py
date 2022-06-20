class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = []
        k = k % len(nums)
        result.extend(nums[len(nums)-k:])
        result.extend(nums[:len(nums)-k+1])
        for i in range(len(nums)):
            nums[i] = result[i]        
