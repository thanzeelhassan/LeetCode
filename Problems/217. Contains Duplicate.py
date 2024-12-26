from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict1 = Counter(nums)
        for i in dict1.values():
            if i != 1:
                return True
        return False
