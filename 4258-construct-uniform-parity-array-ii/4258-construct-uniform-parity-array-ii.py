class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        m = nums1[0]
        hasOdd = False
        for i in nums1:
            if i < m:
                m = i;
            if i % 2 == 1:
                hasOdd = True;
        if m % 2 == 1:
            return True
        return not hasOdd; 
  