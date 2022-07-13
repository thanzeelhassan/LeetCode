class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seen_before = {}
        for i in range(0,len(s)):
            if s[i] in seen_before:
                if t[i] != seen_before[s[i]]:
                    return False
            else:
                if t[i] not in seen_before.values():
                    seen_before[s[i]] = t[i]
                else:
                    return False
        return True