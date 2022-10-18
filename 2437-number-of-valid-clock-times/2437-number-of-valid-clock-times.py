class Solution:
    def countTime(self, time: str) -> int:
        a = time[0]
        b = time[1]
        c = time[2]
        d = time[3]
        e = time[4]
        ans = 1    
        if d == '?':
            ans = ans * 6
        if e == '?':
            ans = ans * 10
        if a == '?' and b =='?':
            ans = ans * 24
        elif a != '?' and b =='?':
            if a == '2':
                ans = ans * 4
            else:
                ans = ans * 10
        elif a == '?' and b !='?':
            if int(b) < 4:
                ans = ans * 3
            else:
                ans = ans * 2
            
        return ans