class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        for item in queries:
            no = 0
            x,y,r = item[0],item[1],item[2]
            for point in points:
                xi,yi = point[0],point[1]
                d = math.sqrt((x - xi)**2 + (y - yi)**2)
                if d <= r:
                    no += 1
            result.append(no)

        return result
