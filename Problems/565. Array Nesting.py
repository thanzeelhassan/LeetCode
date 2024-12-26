class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        largest = 0
        checked = [False] * n
        for i in range(0,n):
            if checked[i]:
                continue
            total = 1
            checked[i] = True
            k = nums[i]

            while not checked[k]:
                total +=1
                checked[i] = True
                k = nums[k]

            largest = max(largest, total)
            if largest >= n / 2:
                return largest
        return largest
