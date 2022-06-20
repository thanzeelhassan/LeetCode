class Solution:
    def reverseWords(self, s: str) -> str:
        array = s.split(" ")
        result = ""
        for item in array:
            result = result + item[::-1] +" "
        return result.strip()
