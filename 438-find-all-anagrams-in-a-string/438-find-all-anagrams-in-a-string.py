from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        pCounter = Counter(p)
        n = len(p)
        sCounter = Counter(s[:n-1])
        
        for i in range(len(s)-n+1):
            sCounter[s[i+n-1]] += 1   # include a new char in the window
            if sCounter == pCounter:    # This step is O(1), since there are at most 26 English letters 
                res.append(i)   # append the starting index
            sCounter[s[i]] -= 1   # decrease the count of oldest char in the window
            if sCounter[s[i]] == 0:
                del sCounter[s[i]]   # remove the count if it is 0
        return res