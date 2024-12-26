# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while(left < right):
            x = (left + right)//2
            b = guess(x)
            if b == 0:
                return x
            if b == 1:
                left = x+1
            else:
                right = x-1
        return left
