class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * (2*n)
        for i in range(0, n):
            res[i] = nums[i]
            res[i + n] = nums[i]

        return res