class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('INF')
        for i in range(1,len(arr)):
            temp = arr[i] - arr[i-1]
            min_diff = min(temp, min_diff)

        result = []
        for i in range(1,len(arr)):
            temp = arr[i] - arr[i-1]
            if temp == min_diff:
                result.append([arr[i-1],arr[i]])

        return result
