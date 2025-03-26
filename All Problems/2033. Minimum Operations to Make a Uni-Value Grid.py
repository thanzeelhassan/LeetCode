class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                nums.append(grid[i][j])

        l = len(nums)
        nums.sort()

        for i in range(0, l-1):
            diff = nums[i] - nums[i+1]
            if diff % x != 0:
                return -1

        result = 0
        temp = int(l / 2)
        for i in range(0, l):
            diff = abs(nums[i] - nums[temp])
            result = result + int(diff / x)

        return result