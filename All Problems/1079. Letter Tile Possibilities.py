class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)
    
        def backtrack(counter):
            total = 0
            for tile in counter:
                if counter[tile] > 0:
                    counter[tile] -= 1 
                    total += 1 + backtrack(counter)
                    counter[tile] += 1 
            return total
        
        return backtrack(count)