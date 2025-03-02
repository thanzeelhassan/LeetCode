class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)

        my_dict = {}
        result = []
        for i in range(n):
            u, v = nums1[i][0], nums1[i][1]
            my_dict[u] = v
        
        for i in range(m):
            u, v = nums2[i][0], nums2[i][1]
            if u in my_dict:
                my_dict[u] += v
            else:
                my_dict[u] = v
            
        for key, value in sorted(my_dict.items()):
            result.append([key, value])
        
        return result
