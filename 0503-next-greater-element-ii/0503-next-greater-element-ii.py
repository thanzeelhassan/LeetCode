class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        '''
        [1,2,3,4,3] [1,2,3,4,3]

        stack = [4,4,3]

        res = [2,3,4,-1,4]

        '''
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(0, 2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                idx = stack.pop()
                res[idx] = nums[i % n]
            stack.append(i % n)
        return res