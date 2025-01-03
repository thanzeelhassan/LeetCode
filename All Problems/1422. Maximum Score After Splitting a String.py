class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        zero_sum = 0
        one_sum = 0
        n = len(s)
        
        if s[0] == '0':
            zero_sum += 1
        
        for i in range(1, n):
            if s[i] == '1':
                one_sum += 1
        
        ans = one_sum + zero_sum
        new_ans = ans

        for i in range(1, n-1):
            if s[i] == '1':
                new_ans = new_ans - 1
            elif s[i] == '0':
                new_ans = new_ans + 1
            
            if new_ans > ans:
                ans = new_ans
        
        return ans
  