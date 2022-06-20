import math
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        s = sum(rolls)
        result = []
        m = len(rolls)
        total =  m + n
        temp = mean * total
        sum_n = temp - s
        avg = sum_n / n
        if avg < 1 or avg > 6:
            return []
        part, rem = divmod(sum_n, n)
        result = [part] * n
        for i in range(rem):
            result[i] += 1
        return result

        
