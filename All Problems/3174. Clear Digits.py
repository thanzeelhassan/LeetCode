class Solution:
    def clearDigits(self, s: str) -> str:
        s = s[::-1]
        n = len(s)
        count_digits = 0
        count_alpha = 0

        ans = "" 
        for i in range(n):
            if s[i].isdigit() == True:
                ans = ans + s[i]
                count_digits = count_digits + 1
            elif s[i].isalpha() == True:
                if count_digits > 0:
                    ans = ans[:-1]
                    count_digits = count_digits - 1
                else:
                    count_alpha = count_alpha + 1
                    ans = ans + s[i]
        return ans[::-1]
        