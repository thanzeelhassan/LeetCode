class Solution:
    def check(self, n):
        a = str(n)
        a = a.split()
        sum = 0
        for digit in str(n):
            item = int(digit)
            sum += item * item
        return sum
    
    def isHappy(self, n: int) -> bool:
        ret = self.check(n)
        my_dict = {}
        my_dict[ret] = 1
        while ret != 1:
            ret = self.check(ret)
            if my_dict.get(ret) != None:
                return False
            else:
                my_dict[ret] = 1
        return True