class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(s)
        m = len(part)

        i = 0
        while(i < n):
            if s[i:i+m] == part:
                s = s[:i] + s[i+m:]
                i = 0
            else:
                i = i + 1
        return s