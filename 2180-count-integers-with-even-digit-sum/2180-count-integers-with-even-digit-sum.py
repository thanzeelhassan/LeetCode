class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for i in range(2,num+1):
            sum = 0
            for digit in str(i): 
                sum += int(digit)  
            if sum%2==0:
                ans = ans + 1
        return ans