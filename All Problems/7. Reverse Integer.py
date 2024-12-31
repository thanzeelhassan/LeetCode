class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == "-":
            x = x[1:]
            result = "".join(reversed(x))
            result = str(int(result))
            result = "-" + result
        else:
            result = "".join(reversed(x))
            result = str(int(result))
        result = int(result)
        if result >= 2**31 or result < -1 * 2**31:
            return 0
        return result
