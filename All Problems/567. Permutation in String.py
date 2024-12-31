class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        dict1 = {}
        for x in range(n):
            if s1[x] in dict1:
                dict1[s1[x]] += 1
            else:
                dict1[s1[x]] = 1
        dict2 = {}
        i = 0
        j = n-1
        for x in range(i,j+1):
            if s2[x] in dict2:
                dict2[s2[x]] +=1
            else:
                dict2[s2[x]] =1

        while(i < m-n):
            if dict1 == dict2:
                return True
            dict2[s2[i]] -= 1
            if dict2[s2[i]] == 0:
                del dict2[s2[i]]

            i = i + 1
            j = j + 1
            if s2[j] in dict2:
                dict2[s2[j]] += 1
            else:
                dict2[s2[j]] = 1

        if dict1 == dict2 :
            return True

        return False
