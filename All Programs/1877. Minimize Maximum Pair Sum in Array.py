class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        n = len(nums)
        for i in range(0,int(n/2)):
            temp = nums[i] + nums[n - i - 1]
            if temp > result:
                result = temp
        return result