class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet_dict = {chr(i): i - 96 for i in range(97, 123)}
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        n = len(words)
        morse = []

        for word in words :
            temp = ""
            for c in word :
                val = alphabet_dict[c]
                temp = temp + morse_code[val - 1]
            morse.append(temp)
        d = {}
        for m in morse :
            if m in d :
                d[m] += 1
            else:
                d[m] = 1
        return len(d)