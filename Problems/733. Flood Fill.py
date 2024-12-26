class Solution:
    def helper(self,image,i,j,newColor,originalColor,rows,columns,dict1):
        temp = str(i) +"_" + str(j)

        if temp in dict1:
            return

        if i < 0 or i >=rows:
            dict1[temp] = 1
            return
        if j < 0 or j >=columns:
            dict1[temp] = 1
            return

        if image[i][j] == originalColor:
            image[i][j] = newColor
            dict1[temp] = 1
            if i > 0:
                self.helper(image,i-1,j,newColor,originalColor,rows,columns,dict1)
            if i < rows - 1:
                self.helper(image,i+1,j,newColor,originalColor,rows,columns,dict1)
            if j > 0:
                self.helper(image,i,j-1,newColor,originalColor,rows,columns,dict1)
            if j < columns - 1:
                self.helper(image,i,j+1,newColor,originalColor,rows,columns,dict1)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # sr = starting row
        # sc = starting column
        # newColor
        originalColor = image[sr][sc]

        rows = len(image)
        columns = len(image[0])

        image[sr][sc] = newColor
        dict1 = {}
        if sr > 0:
            self.helper(image,sr-1,sc,newColor,originalColor,rows,columns,dict1)
        if sr < rows -1 :
            self.helper(image,sr+1,sc,newColor,originalColor,rows,columns,dict1)
        if sc > 0:
            self.helper(image,sr,sc-1,newColor,originalColor,rows,columns,dict1)
        if sc < columns -1:
            self.helper(image,sr,sc+1,newColor,originalColor,rows,columns,dict1)

        return image
        
