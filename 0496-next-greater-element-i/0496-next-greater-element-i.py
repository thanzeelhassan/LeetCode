class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        arr = []
        for x in nums1:
            j = nums2.index(x)
            result = -1
            for i in range(j+1, len(nums2)):
                if nums2[i] > x:
                    result = nums2[i]
                    break
            
            arr.append(result)

        return arr
