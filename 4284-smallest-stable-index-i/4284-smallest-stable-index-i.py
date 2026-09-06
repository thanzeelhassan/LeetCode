class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # make a suffix minimum - one array is needed
        # make a prefix maximum - one integer is enough
        # instability = prefix maximum - suffix minimum

        n = len(nums)
        prefix_max = nums[0]
        suffix_min = [0] * n
        suffix_min[n-1] = nums[n-1]

        for i in range(n-2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i+1])
        
        for i in range(0, n):
            prefix_max = max(prefix_max, nums[i])

            instability = prefix_max - suffix_min[i]

            if instability <= k:
                return i
        
        return -1