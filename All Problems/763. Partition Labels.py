class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []

        def countFrequency(s):
            my_dict = {}

            for c in s:
                if c in my_dict:
                    my_dict[c] += 1
                else:
                    my_dict[c] = 1
            
            return my_dict

        def checkPartition(s, i):
            left_string = s[0:i]
            right_string = s[i:]

            left_dict = countFrequency(left_string)
            right_dict = countFrequency(right_string)

            for key, value in left_dict.items():
                if key in right_dict.keys():
                    return False
            return True
        
        n = len(s)

        for i in range(1, n + 1):
            flag = checkPartition(s, i)
            if flag :
                result.append(i)
                ans = self.partitionLabels(s[i:])
                result.extend(ans)
                break

        return result
