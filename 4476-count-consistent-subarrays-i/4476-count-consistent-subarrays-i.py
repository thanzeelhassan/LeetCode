class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            curr_and = nums[i]
            curr_min = nums[i]
            for j in range(i,n):
                curr_and = curr_and & nums[j]
                curr_min = min(curr_min, nums[j])

                if curr_and == curr_min:
                    ans = ans + 1
        return ans
