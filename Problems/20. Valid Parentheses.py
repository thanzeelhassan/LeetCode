class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        while(len(s)>0):
            if s[0] in ["{","[","("]:
                stack.append(s[0])
                s = s[1:]
            else:
                if len(stack) == 0:
                    return False
                temp = stack.pop()

                if s[0] == ")":
                    if temp!="(":
                        return False
                elif s[0] == "}":
                    if temp!="{":
                        return False
                elif s[0] == "]":
                    if temp!="[":
                        return False
                s = s[1:]

        if len(stack)!=0:
            return False
        return True
