class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        opened = 0
        for c in s:
            if c == '(' and opened > 0:
                result.append(c)
            if c == ')' and opened > 1:
                result.append(c)
            if c == '(':
                opened = opened + 1
            elif c == ')':
                opened = opened - 1
            
        return "".join(result)