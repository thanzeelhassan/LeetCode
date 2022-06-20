from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        dict1 = {}
        for c in s:
            if c in dict1:
                dict1[c] +=1
            else:
                dict1[c] = 1
        dict2 = {}
        for key,value in dict1.items():
            if value in dict2 :
                dict2[value].append(key)
            else:
                dict2[value] = [key]

        result = ""
        for item in sorted(dict2.keys(),reverse = True):
            values = dict2[item]
            for y in values:
                for x in range(item):
                    result = result + y

        return result      
