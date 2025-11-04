class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while(len(s) > 2):
            n = len(s)
            new = ""
            for i in range(0, n-1):
                temp = s[i:i+2]
                print("temp = ", temp)
                a = (int(temp[0]) + int(temp[1])) % 10
                new = new + str(a)
            s = new
        
        if s[0] == s[1]:
            return True
        return False