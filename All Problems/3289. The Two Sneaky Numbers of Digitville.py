class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        my_dict = {}
        
        for i in range(len(nums)):
            if nums[i] in my_dict:
                my_dict[nums[i]] +=1
                ans.append(nums[i])
            else:
                my_dict[nums[i]] =1

        return ans