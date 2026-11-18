class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)
        i = 0
        j = n - 1

        while( i < j):
            edge = j - i
            area = edge * min(height[i], height[j])
            max_area = max(max_area, area)

            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
        
        return max_area