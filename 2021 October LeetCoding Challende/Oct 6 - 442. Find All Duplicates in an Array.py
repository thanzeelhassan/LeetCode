from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        dict1 = Counter(nums)
        for i in dict1:
            if dict1[i] == 2:
                result.append(i)
        return result
