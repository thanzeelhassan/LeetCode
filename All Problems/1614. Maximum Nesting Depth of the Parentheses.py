class Solution:
    def maxDepth(self, s: str) -> int:
        def helper(s):
            list = []
            for i in s:
                if i == '(' :
                    list.append(1)
                elif i == ')' :
                    list.append(-1)

            if len(list) == 0 :
                return 0
            for i in range(1,len(list)):
                list[i] = list[i-1] + list[i]

            return max(list)

        return helper(s)
