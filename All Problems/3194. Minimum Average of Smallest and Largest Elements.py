class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = int(len(nums) / 2)
        averages = []
        for i in range(n):
            u = nums[i]
            v = nums[2 * n - i -1]
            temp = (u + v) / 2
            averages.append(temp)

        return min(averages)