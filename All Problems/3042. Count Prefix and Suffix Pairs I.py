class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        n = len(words)
        for i in range(n - 1):
            for j in range(i + 1, n):
                str1 = words[i]
                str2 = words[j]
                if str2.startswith(str1) and str2.endswith(str1):
                    ans = ans + 1
        return ans