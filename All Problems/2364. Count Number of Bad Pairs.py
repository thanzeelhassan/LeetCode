class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = int(n * (n - 1) / 2) # total number of pairs
        # find good pairs
        good = 0

        my_dict = {}
        for i in range(n):
            my_dict[i] = i - nums[i]

        count_dict = {}

        for key, value in my_dict.items():
            if value in count_dict:
                count_dict[value] = count_dict[value] + 1
            else:
                count_dict[value] = 1

        for key, value in count_dict.items():
            if value > 1:
                good = good + int(value * (value-1) / 2)

        return ans - good