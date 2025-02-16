class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            flag = True
            if (i + k < n):
                if nums[i] <= nums[i+k]:
                    flag = False
            if(i - k > -1):
                if nums[i] <= nums[i-k]:
                    flag = False

            if flag == True :
                ans = ans + nums[i]
        return ans
                