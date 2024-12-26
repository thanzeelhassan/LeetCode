class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for item in operations:
            if item in ["--X", "X--"]:
                x = x - 1
            else:
                x = x + 1

        return x
