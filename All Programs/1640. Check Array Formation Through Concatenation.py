class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for item in pieces:
            if item[0] not in arr:
                return False
            i = arr.index(item[0])
            for j in range(0,len(item)):
                if i >= len(arr):
                    return False
                if item[j] != arr[i]:
                    return False
                i = i + 1
        return True
