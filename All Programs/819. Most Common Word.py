from collections import Counter
import string
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dict1 = {}
        res= []
        paragraph = paragraph.replace("," ," ")
        for i in paragraph.split():
            res.append(i.strip(string.punctuation).lower())
        dict1 = Counter(res)
        max_value = 0
        ret = ""
        for item in dict1:
            if dict1[item] > max_value and item not in banned:
                max_value = dict1[item]
                ret = item
        return ret
