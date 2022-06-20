class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        result = ""
        s_re = s[::-1]
        list1 = []
        for c in s_re:
            if c.isalpha() == True:
                list1.append(c)
        j = 0
        for i in range(0,len(s)):
            if s[i].isalpha() == True:
                result = result + list1[j]
                j = j + 1
            else:
                result = result + s[i]
        return result
