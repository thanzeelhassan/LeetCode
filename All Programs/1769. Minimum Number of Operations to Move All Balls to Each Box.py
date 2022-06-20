class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []
        n = len(boxes)
        left = 0
        right = 0
        temp = 0
        for i in range(1,n):
            if boxes[i] == '1':
                temp = temp + i
                right += 1
        result.append(temp)
        if boxes[0] == '1':
            left += 1
        for i in range(1,n):
            temp = temp + left
            temp = temp - right
            if boxes[i] == '1':
                left +=1
                right -=1
            result.append(temp)
        return result
