import string

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabet_dict = {letter: index + 1 for index, letter in enumerate(string.ascii_uppercase)}
        ans = 0

        while(len(columnTitle) > 0):
            temp = columnTitle[0]
            columnTitle = columnTitle[1:]
            ans = ans +  alphabet_dict[temp] * pow(26, len(columnTitle))
        return ans