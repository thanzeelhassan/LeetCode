class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if len(palindrome) == 1 or len(palindrome) == 0:
            return ""
        for i in range(0,n//2):
            if palindrome[i] != "a":
                return palindrome[:i] + "a" + palindrome[i+1:]
        if n > 1 :
            return palindrome[:-1] + "b"  
