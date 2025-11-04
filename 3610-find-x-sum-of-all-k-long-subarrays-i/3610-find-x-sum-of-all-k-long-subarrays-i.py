class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> int:
        n = len(nums)
        my_dict = {}
        ans = []
        for i in range(n):
            if nums[i] in my_dict:
                my_dict[nums[i]] = my_dict[nums[i]] + 1
            else:
                my_dict[nums[i]] = 1

        if len(my_dict) < k :
            return sum(nums)
        temp = 0
        count = 0
        highest = 0
        my_dict_copy = my_dict.copy()
        while(count < k):
            for key, value in my_dict.items():
                if value > highest:
                    highest = value
                    temp = key
                elif value == highest and key > temp:
                    highest = value
                    temp = key
            ans.append(temp)
            count = count + 1
            highest = 0
            del my_dict[temp]

        ans_sum = 0
        for i in ans:
            ans_sum = ans_sum + i * my_dict_copy[i]
        return ans_sum 

    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = [0] * (n - k + 1)
        
        my_dict = {}

        for i in range(n):
            if nums[i] in my_dict:
                my_dict[nums[i]] = my_dict[nums[i]] + 1
            else:
                my_dict[nums[i]] = 1

        for i in range(0, n - k + 1):
            temp = self.topKFrequent(nums[i:i+k], x)
            ans[i] = temp
        
        return ans
