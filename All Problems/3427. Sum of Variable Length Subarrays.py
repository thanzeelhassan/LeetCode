class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        sum_array = [0] * n
        s = 0
        for i in range(n):
            s = s + nums[i]
            sum_array[i] = s

        temp_array = [0] * n
        for i in range(n):
            u = max(0, i - nums[i])
            v = i
            if u != 0 :
                temp_array[i] = sum_array[v] - sum_array[u-1]
            else:
                temp_array[i] = sum_array[v]
        return sum(temp_array)
        