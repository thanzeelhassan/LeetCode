class Solution:
    def numDistinct(self, s: str, t: str,dict1 = {}) -> int:
        temp = s + "_" + t
        if temp in dict1:
            return dict1[temp]
        if s == t:
            return 1
        if len(s) < len(t):
            return 0
        if len(s) == 0:
            return 0
        if len(t) == 0:
            return 1
        if s[0] == t[0]:
            val = self.numDistinct(s[1:],t[1:],dict1) + self.numDistinct(s[1:],t,dict1)
            dict1[temp] = val
            return val
        else:
            val2 = self.numDistinct(s[1:],t,dict1)
            temp2 = s[1:] + "_" + t
            dict1[temp2] = val2
            return val2
