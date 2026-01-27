class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        diff = float('inf')
        i = 0
        j = k - 1

        while(j < n):
            diff = min(diff, abs(nums[j] - nums[i]))
            i = i + 1
            j = j + 1
        return diff
