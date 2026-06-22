class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        my_dict = {}

        n = len(text)
        for i in range(0,n):
            if text[i] in my_dict:
                my_dict[text[i]] += 1
            else:
                my_dict[text[i]] = 1
        
        if 'b' in my_dict and 'a' in my_dict and 'n' in my_dict and 'l' in my_dict and 'o' in my_dict:
            return min(my_dict['b'], my_dict['a'], my_dict['n'], ceil(my_dict['l']/ 2), ceil(my_dict['o'] / 2));
        else: 
            return 0;