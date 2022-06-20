class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flipCount = 0
        oneCount = 0
        for i in s :
            if i == '0':
                if oneCount == 0 :
                    continue
                else :
                    flipCount = flipCount + 1
            else :
                oneCount = oneCount + 1
            if flipCount > oneCount :
                flipCount = oneCount
        return flipCount
