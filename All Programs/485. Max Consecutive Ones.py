class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_so_far = 0
        temp = 0
        for i in range(0,len(nums)):
            if nums[i] == 1:
                temp+=1
            else:
                if temp > max_so_far:
                    max_so_far = temp
                temp = 0
        if temp > max_so_far:
            max_so_far = temp
        return max_so_far
