class Solution:
    def reverseWords(self, s: str) -> str:
        array = s.split()
        result = ""
        for i in reversed(array):
            result = result + i + " "
        return result.strip()
