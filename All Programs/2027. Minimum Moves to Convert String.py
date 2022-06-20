class Solution:
    def minimumMoves(self, s: str) -> int:
        result = 0
        for i in range(0,len(s)-2):
            if s[i] == "X":
                s = s[:i] + "OOO" + s[i+3:]
                result = result + 1

        if s[-2] == "X" or s[-1] == "X":
            result = result + 1
        return result
            
