class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_frequency = {}

        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                p = nums[i] * nums[j]

                if p in product_frequency:
                    product_frequency[p] += 1
                else: 
                    product_frequency[p] = 1

        ans = 0 

        for key, value in product_frequency.items():
            if value > 1:
                ans = ans + value * 4 * (value -1) 

        return ans