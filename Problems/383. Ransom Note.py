class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1 = collections.Counter(ransomNote)
        dict2 = collections.Counter(magazine)
        if len(dict1-dict2) > 0:
            return False
        return True
