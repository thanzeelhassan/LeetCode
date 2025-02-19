class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        self.getString(ans, "", n, "")
        if k <= len(ans):
            return ans[k-1]
        return ""
    
    def getString(self, ans, s, n, letter):
        if n == 0:
            ans.append(s)
            return
        
        if letter == 'a':
            self.getString(ans, s + "b", n - 1, "b")
            self.getString(ans, s + "c", n - 1, "c")
        elif letter == 'b':
            self.getString(ans, s + "a", n - 1, "a")
            self.getString(ans, s + "c", n - 1, "c")
        elif letter == 'c':
            self.getString(ans, s + "a", n - 1, "a")
            self.getString(ans, s + "b", n - 1, "b")
        else:
            self.getString(ans, s + "a", n - 1, "a")
            self.getString(ans, s + "b", n - 1, "b")
            self.getString(ans, s + "c", n - 1, "c")