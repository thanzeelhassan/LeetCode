class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        array = s.split(" ")
        max_no = float("-INF")
        for item in array:
            if item.isnumeric():
                if int(item) > max_no:
                    max_no = int(item)
                else:
                    return False
        return True
                
