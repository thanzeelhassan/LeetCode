class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater = {}
        stack = []

        for num in nums2 :
            while stack and num > stack[-1]:
                waiting = stack.pop()
                next_greater[waiting] = num
            stack.append(num)
        
        res = []
        for x in nums1:
            res.append(next_greater.get(x, -1))
        
        return res
