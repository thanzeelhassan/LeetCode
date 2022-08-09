class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        n = len(secret)
        bulls = 0
        cows = 0
        
        new_secret = ""
        new_guess = ""
        # do bulls
        for i in range(0,n):
            if guess[i] == secret[i]:
                bulls = bulls + 1
                new_guess += "?"
                new_secret += "!"             
            else:
                new_guess = new_guess + guess[i]
                new_secret = new_secret + secret[i]  
        # do cows
        
        dict1 = collections.Counter(new_secret)
        for i in range(0,n):
            if new_guess[i] == "?":
                continue
            if new_guess[i] in dict1:
                if dict1[new_guess[i]] != 0:
                    cows = cows + 1
                    dict1[new_guess[i]] = dict1[new_guess[i]] - 1         
        ans = ""
        ans = ans + str(bulls) + "A" + str(cows) + "B"
        return ans