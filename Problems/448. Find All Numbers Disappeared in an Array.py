class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(0,n):
            temp = abs(nums[i])
            if nums[temp - 1] > 0:
                nums[temp - 1] = nums[temp - 1] * -1

        result = []
        for i in range(0,n):
            if nums[i] > 0:
                result.append(i+1)

        return result
