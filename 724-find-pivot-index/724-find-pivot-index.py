class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        i = 0
        j = s
        x = 0
        while(x<len(nums)):
            if i == j-nums[x]:
                return x
            i = i + nums[x]
            j = j - nums[x]
            x = x + 1
        if i == j-nums[x-1]:
            return x-1
        return -1