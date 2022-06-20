class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1

        while(i<j):
            temp = (i+j)//2
            if target == nums[temp]:
                return temp
            elif target > nums[temp]:
                i = temp + 1
            else:
                j = temp - 1

        if target <= nums[i]:
            return i
        elif target > nums[i]:
            return i+1
