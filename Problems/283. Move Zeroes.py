class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                j = j + 1
