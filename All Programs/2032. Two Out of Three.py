from collections import Counter
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        dict1 = {}
        result = []
        nums1= set(nums1)
        nums2= set(nums2)
        nums3= set(nums3)
        for i in nums1:
            dict1[i] = 1
        for i in nums2:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        for i in nums3:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        for item in dict1:
            if dict1[item] >= 2:
                result.append(item)
        return result
