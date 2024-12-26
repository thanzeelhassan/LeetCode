class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        pointer1 = 0
        pointer2 = len(nums)-1
        while(pointer1 <= pointer2):
            if nums[pointer1] ** 2 < nums[pointer2] ** 2:
                result.append(nums[pointer2] ** 2)
                pointer2 = pointer2 - 1
            else:
                result.append(nums[pointer1] ** 2)
                pointer1 = pointer1 + 1
        result.reverse()
        return result
