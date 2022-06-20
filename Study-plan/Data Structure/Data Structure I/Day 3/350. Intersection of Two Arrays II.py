from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = Counter(nums1)
        dict2 = Counter(nums2)
        result = []
        for item in dict1:
            if item in dict2:
                n = min(dict1[item], dict2[item])
                for i in range(n):
                    result.append(item)
        return result
