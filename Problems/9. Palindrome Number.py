class Solution:
    def isPalindrome(self, x: int) -> bool:
        s1 = str(x)
        s2 = s1[::-1]
        if s1 == s2:
            return True
        return False
