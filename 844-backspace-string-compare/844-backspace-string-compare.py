class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_real = ""
        t_real = ""
        
        i = 0
        j = 0
        n = len(s)
        while(i<n):
            if s[i] != "#":
                s_real = s_real + s[i]
                i = i + 1
                j = j + 1
            else:
                s_real = s_real[:-1]
                i = i + 1
        t_real = ""
        i = 0
        j = 0
        n = len(t)
        while(i<n):
            if t[i] != "#":
                t_real = t_real + t[i]
                i = i + 1
                j = j + 1
            else:
                t_real = t_real[:-1]
                i = i + 1
        if s_real == t_real:
            return True
        return False