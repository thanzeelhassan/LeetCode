class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        result = [0,0]
        my_dict = {chr(i): i - 96 for i in range(97, 123)}
        n = len(s)
        current = 0
        lines = 1
        for i in range(n):
            c = s[i]
            value = my_dict[c]

            width = widths[value - 1]
            if current + width > 100 :
                lines = lines + 1
                current = width
            else :
                current = current + width
            
        result[0] = lines
        result[1] = current
        return result