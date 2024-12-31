class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        div = k % n
        ans = ""
        for i in range(n):
            temp = i + div
            if temp >= n:
                temp = temp % n
            ans = ans + s[temp]
        return ans