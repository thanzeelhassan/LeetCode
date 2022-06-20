class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(0,rowIndex+1):
            temp = [1] * (i+1)
            if i > 1:
                arr = result[-1]
                for x in range(1,i):
                    temp[x] = arr[x-1] + arr[x]

            result.append(temp)
        return result[-1]
