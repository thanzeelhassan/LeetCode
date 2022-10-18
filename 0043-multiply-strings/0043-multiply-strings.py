def splitNum(num):           
    num = [int(d) for d in str(num)]
    pow = len(num)-1
    for i in range(len(num)):
        num[i] = (num[i]*10**pow)
        pow -= 1                
    return num
        
class Solution:
    def multiply(self, num1: str, num2: str) -> str:        
        n1 = splitNum(num1)
        n2 = splitNum(num2)
        ans = 0
        for x in n1:
            for y in n2:
                ans = ans + x * y
        return str(ans)