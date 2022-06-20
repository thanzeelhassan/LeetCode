class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        for x in range(len(nums1)):
            ind = nums2.index(nums1[x])
            for i in range(ind+1, len(nums2)):
                if nums2[i] > nums1[x]:
                    result[x] = nums2[i]
                    break
        return result
