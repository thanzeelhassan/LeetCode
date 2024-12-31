from collections import Counter
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()
        dict1 = Counter(arr)
        for i in dict1.copy():
            if i in dict1:
                if 2*i in dict1:
                    if i == 0 :
                        if dict1[i] % 2 == 0:
                            del dict1[i]
                        else:
                            return 0
                    else :
                        a = dict1[i]
                        b = dict1[2*i]
                        if dict1[i] == 1:
                            del dict1[i]
                        else :
                            dict1[i] -= min(a,b)
                            if dict1[i] == 0:
                                del dict1[i]
                        if dict1[2*i] == 1:
                            del dict1[2*i]
                        else :
                            dict1[2*i] -= min(a,b)
                            if dict1[2*i] == 0:
                                del dict1[2*i]

        if len(dict1) == 0 :
            return 1
        else :
            return 0
