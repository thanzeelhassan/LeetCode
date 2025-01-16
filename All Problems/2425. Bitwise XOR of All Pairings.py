class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        ans = 0
        if n % 2 == 0 and m % 2 == 0:
            return 0
        elif n % 2 == 0:
            for i in range(n):
                ans = ans ^ nums1[i]
        elif m % 2 == 0:
            for i in range(m):
                ans = ans ^ nums2[i]
        else:
            for i in range(n):
                ans = ans ^ nums1[i]
            for i in range(m):
                ans = ans ^ nums2[i]
        return ans
