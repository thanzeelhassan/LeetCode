class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [-1] * n
        for i in range(n):
            for k in range(1, n):            # look at the next n-1 elements
                j = (i + k) % n              # % n wraps around to the start
                if nums[j] > nums[i]:
                    ans[i] = nums[j]
                    break
        return ans