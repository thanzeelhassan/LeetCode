class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        l = len(words)
        ans = [0] * n
        prefix_sum = [0] * l
        vowels = {'a', 'e', 'i', 'o', 'u'}
        sum = 0
        for i in range(l):
            current_word = words[i]
            if (current_word[0] in vowels and current_word[-1] in vowels):
                sum += 1
            prefix_sum[i] = sum
        
        for i in range(n):
            current_query = queries[i]
            l, r = current_query[0], current_query[1]
            if l == 0 :
                ans[i] = prefix_sum[r] - 0
            else:
                ans[i] = prefix_sum[r] - prefix_sum[l - 1]

        return ans