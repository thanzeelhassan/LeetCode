class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        my_dict = {}
        largest = -1
        for i in nums:
            if i not in my_dict.keys():
                my_dict[i] = 1
            neg_i = -1 * i
            if neg_i in my_dict.keys():
                temp = max(i,neg_i)
                if temp > largest:
                    largest = temp                    
        return largest