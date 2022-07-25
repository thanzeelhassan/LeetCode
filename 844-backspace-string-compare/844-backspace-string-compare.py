class Solution:
    def get_real(self, string):
        string_real = ""
        i = 0
        j = 0
        n = len(string)
        while(i<n):
            if string[i] != "#":
                string_real = string_real + string[i]
                i = i + 1
                j = j + 1
            else:
                string_real = string_real[:-1]
                i = i + 1
        return string_real    
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_real = self.get_real(s)     
        t_real = self.get_real(t)
        if s_real == t_real:
            return True
        return False