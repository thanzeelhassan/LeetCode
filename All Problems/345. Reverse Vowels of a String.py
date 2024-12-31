class Solution:
    def reverseVowels(self, s: str) -> str:
        array = []
        vowels = ["a","e","i","o","u","A","E","O","I","U"]
        for c in range(len(s)):
            if s[c] in vowels:
                array.append(c)

        array = array[::-1]
        x = 0
        result = ""
        for i in range(len(s)):
            if s[i] not in vowels:
                result = result + s[i]
            else:
                result = result + s[array[x]]
                x = x + 1

        return result
