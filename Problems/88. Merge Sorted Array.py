class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        result = []
        while(i< m and j < n):
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i = i + 1
            else:
                result.append(nums2[j])
                j = j + 1
        if i == m :
            for x in range(j,n):
                result.append(nums2[x])

        elif j == n :
            for x in range(i,m):
                result.append(nums1[x])

        for x in range(n+m):
            nums1[x] = result[x]
