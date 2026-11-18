class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        i = 0
        j = n - 1

        while(i < j):
            temp = (i + j) // 2
            if nums[temp] == target:
                return temp
            elif nums[temp] < target:
                i = temp + 1
            else:
                j = temp - 1
        
        if nums[j] == target:
            return j
        return -1
