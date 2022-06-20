class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = []
        n2 = []
        for i in num1 :
            n1.append(i)
        for i in num2:
            n2.append(i)
        n1.reverse()
        n2.reverse()
        x = 0
        y = 0
        for i in range(0,len(n1)):
            x = x + int(n1[i]) * 10 **i
        for i in range(0,len(n2)):
            y = y + int(n2[i]) * 10 **i
        z = x+y

        return str(z) 
