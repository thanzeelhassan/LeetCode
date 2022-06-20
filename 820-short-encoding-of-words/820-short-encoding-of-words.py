class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        s = ""
        words.sort(key=len, reverse = True)
        for x in words:
            if x+"#" not in s:
                s = s + x+"#"
        return len(s)