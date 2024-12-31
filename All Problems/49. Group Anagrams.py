from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        big_dict = {}
        for item in strs:
            i = strs.index(item)
            temp = Counter(item)
            dict1 = dict(temp)
            dict1 = sorted(dict1.items())
            key = ""
            for x in dict1:
                a = x[0]
                b = x[1]
                key = key+a+str(b)
            if key in big_dict :
                big_dict[key].append(i)
            else :
                big_dict[key] = [i]
        for item in big_dict.values() :
            temp = []
            for i in item:
                temp.append(strs[i])
            result.append(temp)
        return result
