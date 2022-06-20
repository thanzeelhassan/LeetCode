class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 0
        for i in range(0,len(digits)):
            n = n * 10 + digits[i]
        n = n + 1
        ans = []
        n_string = str(n)
        for i in n_string:
            ans.append(int(i))
        return ans
            
        