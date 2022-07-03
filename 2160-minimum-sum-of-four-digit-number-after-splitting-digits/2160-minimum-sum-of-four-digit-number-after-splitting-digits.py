class Solution:
    def minimumSum(self, num: int) -> int:
        n = str(num)
        arr = []
        for i in n:
            arr.append(int(i))
        
        arr.sort()
        new1 = arr[0]
        new2 = arr[1]
        new1 = new1 * 10 + arr[2]
        new2 = new2 * 10 + arr[3]
        return new1 + new2