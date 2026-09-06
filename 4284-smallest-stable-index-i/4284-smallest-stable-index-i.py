class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        ans = -1
        
        max_so_far = -1
        min_so_far = min(nums)

        n = len(nums)
        for i in range(0, n):
            max_so_far = max(max_so_far, nums[i])
            min_so_far = min(nums[i:n])

            instability = max_so_far - min_so_far

            if instability <= k:
                ans = i
                return ans
        
        return ans