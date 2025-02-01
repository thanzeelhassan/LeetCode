class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        lastSeen = None

        a = nums[0]
        if a % 2 == 0:
            lastSeen = 0
        else:
            lastSeen = 1

        for i in range(1, len(nums)):
            a = nums[i]
            if a % 2 == 0:
                if lastSeen == 0:
                    return False
                else:
                    lastSeen = 0
            elif lastSeen == 1:
               return False
            else:
                lastSeen = 1
        return True