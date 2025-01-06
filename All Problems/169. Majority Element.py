class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        my_dict = {}
        for i in nums:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
            
            if my_dict[i] > n / 2:
                return i
        
        return 0