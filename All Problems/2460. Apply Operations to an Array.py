class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i in range(0, n-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
        j = 0
        for i in range(0, n):
            if nums[i] != 0:
                result[j] = nums[i]
                j = j + 1

        return result