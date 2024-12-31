class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = collections.Counter(s)
        for i,j in dict1.items():
            if j == 1:
                return s.index(i)
        return -1
