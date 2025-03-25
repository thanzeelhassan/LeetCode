class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # [start_x, start_y, end_x, end_y]
        # [0, 1, 2, 3]
        # check x
        rectangles.sort()

        gap_counts_x = 0
        furthest_end = rectangles[0][2]
        m = len(rectangles)
        
        for i in range(1, m):
            if furthest_end <= rectangles[i][0]:
                gap_counts_x = gap_counts_x + 1
   
            furthest_end = max(furthest_end, rectangles[i][2])
        
        # check y
        rectangles.sort(key = lambda x: x[1])
        
        gap_counts_y = 0
        furthest_end = rectangles[0][3]
        m = len(rectangles)
        
        for i in range(1, m):
            if furthest_end <= rectangles[i][1]:
                gap_counts_y = gap_counts_y + 1
   
            furthest_end = max(furthest_end, rectangles[i][3])
        
        if gap_counts_x >= 2 or gap_counts_y >= 2:
            return True
        return False


