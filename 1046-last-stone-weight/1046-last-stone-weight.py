class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        
        while len(stones) > 1:
            s = stones[-1] - stones[-2]
            del stones[-2:]
           # insert the new stone at the correct position
            if s != 0:  bisect.insort(stones, s)
        
        if len(stones) == 0:    return 0
        else:   return stones[0]
        
