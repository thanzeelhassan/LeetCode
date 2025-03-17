class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        my_dict = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in my_dict:
                my_dict[nums[i]] = my_dict[nums[i]] + 1
            else:
                my_dict[nums[i]] = 1
        
        for key, value in my_dict.items():
            if value % 2 != 0:
                return False
        return True
