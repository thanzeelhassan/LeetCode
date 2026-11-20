class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        array = [0] * 50
        seen_so_far = 0
        n = len(nums)

        for i in range(n-1, -1, -1):
            temp = nums[i] 
            if array[temp-1] == 0 and temp <= k :
                array[temp-1] = 1
                seen_so_far += 1
            
            if seen_so_far == k:
                return n - i
            
        return -1
                   

        