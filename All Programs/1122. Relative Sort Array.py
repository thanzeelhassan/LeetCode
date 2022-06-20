from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        dict1 = Counter(arr1)
        dict2 = Counter(arr2)
        r = list(dict1.keys()-dict2.keys())
        r.sort()
        for item in arr2:
            n = dict1[item]
            for i in range(n):
                result.append(item)
        for item in r:
            n = dict1[item]
            for i in range(n):
                result.append(item)
        return result
