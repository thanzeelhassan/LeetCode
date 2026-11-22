class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        my_dict = {}

        n = len(nums)

        for i in range(n):
            if nums[i] in my_dict :
                return True
            else:
                my_dict[nums[i]] = 1
        
        return False