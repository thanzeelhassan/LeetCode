class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        arr = []
        m = len(bank)
        for i in range(0, m):
            count = 0
            for j in bank[i]:
                if j == '1':
                    count = count + 1
            if count != 0:
                arr.append(count)
        ans = 0
        s = len(arr)
        for i in range(0, s - 1):
            ans = ans + arr[i] * arr[i+1]
        return ans