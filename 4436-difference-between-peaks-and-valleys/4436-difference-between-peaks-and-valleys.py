class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        sum_of_peaks = 0
        sum_of_valleys = 0

        n = len(nums)

        for i in range(1, n-1):
            if ((nums[i] > nums[i-1]) and (nums[i] > nums[i+1])):
                sum_of_peaks += nums[i]
            elif ((nums[i] < nums[i-1]) and (nums[i] < nums[i+1])):
                sum_of_valleys += nums[i]
        
        return  sum_of_peaks - sum_of_valleys